import os,json
from pathlib import Path
def json_format(all_pred_boxes,all_gt_boxes,all_img_info,algorithm):
	json_res_data = []
	json_targ_annotations = []
	img_info=[]
	pred_ids=0
	gt_ids=0
	for inds,(pred_boxes,gt_boxes,img_infos) in enumerate(zip(all_pred_boxes,all_gt_boxes,all_img_info)):
		pred_boxes=pred_boxes.copy()
		gt_boxes=gt_boxes.copy()
		pred_boxes[:,2:4] -=pred_boxes[:,:2]
		areas=(gt_boxes[:, 3] - gt_boxes[:, 1]) * (gt_boxes[:, 2] - gt_boxes[:, 0])
		gt_boxes[:,2:4] -=gt_boxes[:,:2]
		for box_ids,box in enumerate(pred_boxes):
			box[0],box[1],box[2],box[3] = float(box[0]),float(box[1]),float(box[2]),float(box[3])
			json_data = {"image_id": img_infos[2],"category_id":1,"bbox":box[0:4].tolist(),'score':float(box[4].item()),'id':pred_ids}
			json_res_data.append(json_data)
			pred_ids+=1
		for box_ids,(box,area) in enumerate(zip(gt_boxes,areas)):
			box[0],box[1],box[2],box[3] = float(box[0]),float(box[1]),float(box[2]),float(box[3])
			json_data = {"image_id": img_infos[2],"category_id":1,"bbox":box[0:4].tolist(),'area':area.tolist(),'iscrowd':0,'id':gt_ids}
			json_targ_annotations.append(json_data)
			gt_ids+=1
		img_info.append({'width':img_infos[1],'height':img_infos[0],'id':inds})
	Path(os.path.join('LRP','output',algorithm)).mkdir(parents=True, exist_ok=True)
	res_write = open(os.path.join('LRP','output',algorithm,'results.json'),'w')
	json.dump(json_res_data, res_write)
	targ_data = {}
	targ_data['info'] = {'description': 'COCO Data format', 'url': 'http://cocodataset.org', 'version': '1.0', 'year': 2017, 'contributor': 'COCO Consortium', 'date_created': '2017/09/01'}
	targ_data['images'] = img_info
	targ_data['annotations'] = json_targ_annotations
	targ_data['categories'] = [{'supercategory': 'person', 'id': 1, 'name': 'person'}]
	res_write = open(os.path.join('LRP','output',algorithm,'targets.json'),'w')
	json.dump(targ_data, res_write)
	return