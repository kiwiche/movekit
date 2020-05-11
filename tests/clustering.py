import unittest
from src.movekit.clustering import *

class Test_clustering(unittest.TestCase):
	def test_dtw_matrix(self):

		ref = pd.DataFrame({312:
			{312: 0.0, 511: 74.09067953165595, 607: 38.03365928918165, 811: 80.77636691446091,
			 905: 104.2485347931366}, 511: {312: 74.09067953165595, 511: 0.0, 607: 61.20636468753354,
			811: 154.28892643064987, 905: 46.62598844408468}, 607:
			{312: 38.03365928918165, 511: 61.20636468753354, 607: 0.0, 811: 110.74896336324917, 905: 103.84620569989656},
			811: {312: 80.77636691446091, 511: 154.28892643064987, 607: 110.74896336324917, 811: 0.0,
			905: 177.42829599543492}, 905: {312: 104.2485347931366, 511: 46.62598844408468,
			607: 103.84620569989656, 811: 177.42829599543492, 905: 0.0}})

		inp = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2},
							'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811, 9: 905},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76},
							'distance': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
							'average_speed': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
							'average_acceleration': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
							'direction': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}})
		case = dtw_matrix(inp)
		pd.testing.assert_frame_equal(ref,case, check_dtype=False)



	def test_df_cluster(self):
		inp = {'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2},
			   'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811, 9: 905},
			   'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01, 7: 390.25,
					 8: 445.48, 9: 365.86}, 'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37,
												  6: 428.82, 7: 405.89, 8: 412.26, 9: 451.76},
			   'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817, 6: 0.04472135955000596,
							7: 0.07999999999998408, 8: 0.45967379738247277, 9: 0.19999999999998863},
			   'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817,
								 6: 0.04472135955000596, 7: 0.07999999999998408, 8: 0.45967379738247277,
								 9: 0.19999999999998863},
			   'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817,
										6: 0.04472135955000596, 7: 0.07999999999998408, 8: 0.45967379738247277,
										9: 0.19999999999998863},
			   'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643265535814, 6: 63.434948822954574,
							 7: 180.0, 8: 44.1185960034137, 9: 180.0},
			   'stopped': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}}
		inp = pd.DataFrame(inp)
		ref = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2},
							'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607,
										  8: 811, 9: 905},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76},
							'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817,
										 6: 0.04472135955000596, 7: 0.07999999999998408, 8: 0.45967379738247277,
										 9: 0.19999999999998863},
							'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817,
											  6: 0.04472135955000596, 7: 0.07999999999998408, 8: 0.45967379738247277,
											  9: 0.19999999999998863},
							'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.39051248379531817,
													 6: 0.04472135955000596, 7: 0.07999999999998408,
													 8: 0.45967379738247277, 9: 0.19999999999998863},
							'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643265535814,
										  6: 63.434948822954574, 7: 180.0, 8: 44.1185960034137, 9: 180.0},
							'stopped': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1},
							'cluster': {0: 2, 1: 0, 2: 2, 3: 1, 4: 0, 5: 2, 6: 0, 7: 2, 8: 1, 9: 0},
							'ClustCenter': {0: [397.81, 411.825, 0.0, 0.0], 1: [368.025, 440.27, 0.0, 0.0],
											2: [397.81, 411.825, 0.0, 0.0], 3: [445.15, 411.94, 0.0, 0.0],
											4: [368.025, 440.27, 0.0, 0.0],
											5: [397.78, 411.63, 0.23525624189765112,0.23525624189765112],
											6: [367.935, 440.28999999999996, 0.12236067977499729, 0.12236067977499729],
											7: [397.78, 411.63, 0.23525624189765112, 0.23525624189765112],
											8: [445.48, 412.26, 0.45967379738247277, 0.45967379738247277],
											9: [367.935, 440.28999999999996, 0.12236067977499729, 0.12236067977499729]},
							'centroid_x': {0: 397.81, 1: 368.025, 2: 397.81, 3: 445.15, 4: 368.025, 5: 397.78,
										   6: 367.935, 7: 397.78, 8: 445.48, 9: 367.935},
							'centroid_y': {0: 411.825, 1: 440.27, 2: 411.825, 3: 411.94, 4: 440.27, 5: 411.63,
										   6: 440.28999999999996, 7: 411.63, 8: 412.26, 9: 440.28999999999996},
							'centroid_distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.23525624189765112,
												  6: 0.12236067977499729, 7: 0.23525624189765112,
												  8: 0.45967379738247277, 9: 0.12236067977499729},
							'centroid_average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.23525624189765112,
													   6: 0.12236067977499729, 7: 0.23525624189765112,
													   8: 0.45967379738247277, 9: 0.12236067977499729}})

		case = ts_cluster(inp, 3, ["x", "y", "distance", "average_speed"])

		pd.testing.assert_frame_equal(ref, case)

	def test_heading_difference(self):
		ref = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3},
							'animal_id':{0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811,
										 9: 905, 10: 312},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86, 10: 405.31},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76, 10: 417.07},
							'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.3905, 6: 0.0447, 7: 0.08,
										 8: 0.4597, 9: 0.2, 10: 0.3},
							'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0,
											  8: 0.0, 9: 0.0, 10: 0.0},
							'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0,
													 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0},
							'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643, 6: 63.4349,
										  7: 180.0, 8: 44.1186, 9: 180.0, 10: -90.0},
							'stopped': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0},
							'x_centroid': {0: 395.364, 1: 395.364, 2: 395.364, 3: 395.364, 4: 395.364, 5: 395.382,
										   6: 395.382, 7: 395.382, 8: 395.382, 9: 395.382, 10: 405.31},
							'y_centroid': {0: 423.226, 1: 423.226, 2: 423.226, 3: 423.226, 4: 423.226, 5: 423.22,
										   6: 423.22, 7: 423.22, 8: 423.22, 9: 423.22, 10: 417.07},
							'medoid': {0: 312, 1: 312, 2: 312, 3: 312, 4: 312, 5: 312, 6: 312, 7: 312, 8: 312, 9: 312,
									   10: 312},
							'distance_to_centroid': {0: 11.331, 1: 25.975, 2: 18.052, 3: 51.049, 4: 40.901, 5: 11.523,
													 6: 25.983, 7: 18.074, 8: 51.283, 9: 41.062, 10: 0.0},
							'centroid_direction': {0: None, 1: None, 2: None, 3: None, 4: None, 5: -18.43494882281345,
												   6: -18.43494882281345, 7: -18.43494882281345, 8: -18.43494882281345,
												   9: -18.43494882281345, 10: -31.77656326002603},
							'heading_difference': {0: None, 1: None, 2: None, 3: None, 4: None, 5: -68.62935117718655,
												   6: 81.86984882281342, 7: -161.56505117718655, 8: 62.55354882281347,
												   9: -161.56505117718655, 10: -58.22343673997398}})
		inp = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3},
							'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811,
										  9: 905, 10: 312},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86, 10: 405.31},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76, 10: 417.07},
							'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.3905, 6: 0.0447, 7: 0.08,
										 8: 0.4597, 9: 0.2, 10: 0.3},
							'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0,
											  8: 0.0, 9: 0.0, 10: 0.0},
							'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0,
													 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0},
							'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643, 6: 63.4349,
										  7: 180.0, 8: 44.1186, 9: 180.0, 10: -90.0},
							'stopped': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}})
		case = get_heading_difference(inp)
		pd.testing.assert_frame_equal(ref,case)


	def test_polarization(self):
		ref = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3}, 'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811, 9: 905, 10: 312}, 'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01, 7: 390.25, 8: 445.48, 9: 365.86, 10: 405.31}, 'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82, 7: 405.89, 8: 412.26, 9: 451.76, 10: 417.07}, 'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.3905, 6: 0.0447, 7: 0.08, 8: 0.4597, 9: 0.2, 10: 0.3}, 'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0}, 'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0}, 'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643, 6: 63.4349, 7: 180.0, 8: 44.1186, 9: 180.0, 10: -90.0}, 'stopped': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, 'polarization': {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.24883852303044318, 6: 0.24883852303044318, 7: 0.24883852303044318, 8: 0.24883852303044318, 9: 0.24883852303044318, 10: 1.0}})
		inp = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3},
							'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811,
										  9: 905, 10: 312},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86, 10: 405.31},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76, 10: 417.07},
							'distance': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.3905, 6: 0.0447, 7: 0.08,
										 8: 0.4597, 9: 0.2, 10: 0.3},
							'average_speed': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0,
											  8: 0.0, 9: 0.0, 10: 0.0},
							'average_acceleration': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0,
													 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0},
							'direction': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -87.0643, 6: 63.4349,
										  7: 180.0, 8: 44.1186, 9: 180.0, 10: -90.0},
							'stopped': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}})
		case = compute_polarization(inp)
		pd.testing.assert_frame_equal(ref, case)

	def test_voronoi(self):
		ref_area = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2},
								 'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811,
											   9: 905},
								 'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
									   7: 390.25, 8: 445.48, 9: 365.86},
								 'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
									   7: 405.89, 8: 412.26, 9: 451.76},
								 'area_voronoi': {0: 2414.225693024696, 1: float("inf"), 2: float("inf"),
												  3: float("inf"), 4: float("inf"), 5: 2389.8757249973805,
												  6: float("inf"), 7: float("inf"), 8: float("inf"), 9: float("inf")}})
		ref_points = [[[405.29, 417.76],
					  [369.99, 428.78],
					  [390.33, 405.89],
					  [445.15, 411.94],
					  [366.06, 451.76]],
					 [[405.31, 417.37],
					  [370.01, 428.82],
					  [390.25, 405.89],
					  [445.48, 412.26],
					  [365.86, 451.76]]]

		inp = pd.DataFrame({'time': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2},
							'animal_id': {0: 312, 1: 511, 2: 607, 3: 811, 4: 905, 5: 312, 6: 511, 7: 607, 8: 811,
										  9: 905},
							'x': {0: 405.29, 1: 369.99, 2: 390.33, 3: 445.15, 4: 366.06, 5: 405.31, 6: 370.01,
								  7: 390.25, 8: 445.48, 9: 365.86},
							'y': {0: 417.76, 1: 428.78, 2: 405.89, 3: 411.94, 4: 451.76, 5: 417.37, 6: 428.82,
								  7: 405.89, 8: 412.26, 9: 451.76}})

		area, diagrams = voronoi_diagram(inp)

		# Generating list of points from diagrams of the two tested time points
		pointlst = []
		for i in diagrams:
			pointlst.append(i.points.tolist())

		# testing area dataframe
		pd.testing.assert_frame_equal(ref_area, area)

		# testing points lists
		self.assertListEqual(ref_points, pointlst)

if __name__ == '__main__':
    unittest.main()