import os

from pycocotools.coco import COCO
from pycocotools.cocoevalLRP import COCOevalLRP
# from boxmapDist import calc_boxmap_FP_FN

def calc_LRP(algorithm,tau=0.50):
	#initialize COCO ground truth api
	annFile = os.path.join('./','LRP','output',algorithm,"targets.json")
	cocoGt=COCO(annFile)
	#initialize COCO detections api
	resFile = os.path.join('./','LRP','output',algorithm,"results.json")
	#resFile = os.path.join(root_path,algorithm,"results.json")
	cocoDt=cocoGt.loadRes(resFile)
	# running evaluation
	DetailedLRPResultNeeded=0
	cocoEvalLRP = COCOevalLRP(cocoGt,cocoDt,tau)
	cocoEvalLRP.evaluate()
	cocoEvalLRP.accumulate()
	cocoEvalLRP.summarize(DetailedLRPResultNeeded)
# def calc_BoxmapDist():
# 	gt_paths = glob.glob(os.path.join(root_path,algorithm,"boxmap/gt","*"))
# 	pred_paths = glob.glob(os.path.join(root_path,algorithm,"boxmap/pred","*"))
# 	FP_mean, FN_mean = calc_boxmap_FP_FN(gt_paths,pred_paths)
# 	print("FP_mean: {0}, FN_mean: {1}".format(FP_mean,FN_mean))
# calc_LRP(.50)
# calc_BoxmapDist()
