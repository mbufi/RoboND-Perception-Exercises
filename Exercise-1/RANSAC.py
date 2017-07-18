# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')

# Voxel Grid filter ###################################################
# Create a VoxelGrid filter object for our input point cloud to reduce number of points
vox = cloud.make_voxel_grid_filter()

# choose a voxel (also known as leaf) size
# Note: 1  = vocel is 1 cubic meter.
# Therefore, go down to a small voxel to retain important details.
LEAF_SIZE = .01

# Set the voxel size
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

# Cakk the filter function to obtain the resultatn downsampled point cloud
cloud_filtered = vox.filter()
filename = 'voxel_downsampled.pcd'
pcl.save(cloud_filtered, filename)


# PassThrough filter ###################################################
# Pass Through Filter works much like a cropping tool, which allows you to crop any given 3D point cloud by specifying an axis with cut-off values along that axis.

# Create a PassThrough filter object.
passthrough = cloud_filtered.make_passthrough_filter()

# Assign axis and range to the passthrough filter object.
filter_axis = 'z'
passthrough.set_filter_field_name (filter_axis)
#extracting only tables and objects.
axis_min = 0.6
axis_max = 1.1
passthrough.set_filter_limits (axis_min, axis_max)

# Finally use the filter function to obtain the resultant point cloud. 
cloud_filtered = passthrough.filter()
filename = 'pass_through_filtered.pcd'
pcl.save(cloud_filtered, filename)

# RANSAC plane segmentation ###################################################
# Random Sample Consensus
# RANSAC is an algorithm, that you can use to identify points in your dataset that belong to a particular model
# We need to remove the table, so look for planes to remove

# Create the segmentation object
seg = cloud_filtered.make_segmenter()

# Set the model you wish to fit 
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)

# Max distance for a point to be considered fitting the model
# Experiment with different values for max_distance 
# for segmenting the table
max_distance = 0.01
seg.set_distance_threshold(max_distance)

# Call the segment function to obtain set of inlier indices and model coefficients
inliers, coefficients = seg.segment()


# Extract inliers (table) ###################################################
extracted_inliers = cloud_filtered.extract(inliers, negative=False)
filename = 'extracted_inliers.pcd'
pcl.save(extracted_inliers, filename)


# Save pcd for table ###################################################
# pcl.save(cloud, filename) ###################################################


# Extract outliers (table top objects) ###################################################
extracted_outliers = cloud_filtered.extract(inliers, negative=True)
filename = 'extracted_outliers.pcd'
pcl.save(extracted_outliers, filename)

# Save pcd for tabletop objects ###################################################


