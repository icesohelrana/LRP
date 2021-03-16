from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pdb
def calc_boxmap_FP_FN(gt_paths,pred_paths):
	FP_ratios = []
	FN_ratios = []
	for gt_path,pred_path in zip(gt_paths,pred_paths):
		gt_im = Image.open(gt_path)
		pred_im = Image.open(pred_path)
		gt_im = np.array(gt_im,dtype=np.int16)
		pred_im = np.array(pred_im,dtype=np.int16)
		boxmap_dist = gt_im-pred_im
		total_pixels = boxmap_dist.shape[0]*boxmap_dist.shape[1]
		FP_pixels = len(boxmap_dist[boxmap_dist<0])
		FN_pixels = len(boxmap_dist[boxmap_dist>0])
		# TP_pixels = len(boxmap_dist[boxmap_dist==0])
		FP_ratio = FP_pixels/total_pixels
		FN_ratio = FN_pixels/total_pixels
		FP_ratios.append(FP_ratio)
		FN_ratios.append(FN_ratio)
	FP_ratios = np.array(FP_ratios)
	FN_ratios = np.array(FN_ratios)
	FP_mean = FP_ratios.mean()
	FN_mean = FN_ratios.mean()
	return FP_mean, FN_mean
def dist(gt_boxmap,pred_boxmap):
	dist_boxmap = gt_boxmap-pred_boxmap