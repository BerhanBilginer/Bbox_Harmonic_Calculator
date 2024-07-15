import os 
import cv2

def BboxHarmonicMeanCalculator(labels_source : str, images_source : str):

    area = []

    for image in os.listdir(images_source):
        image_path = os.path.join(images_source, image)
        if image_path is not None:
            img0 = cv2.imread(image_path)
            img0_h, img0_w, _ = img0.shape

    for label in os.listdir(labels_source):
        label_path = os.path.join(labels_source, label)
        if label.endswith('.txt'):
            with open(label_path, 'r') as f:
                lines = f.readlines()

            for line in lines:
                values = line.split()
                x_center, y_center, bbox_width, bbox_height = map(float, values[1:])

                abs_bbox_width = max(float(bbox_width * img0_w), 0)
                abs_bbox_height = max(float(bbox_height * img0_h), 0)

                bbox_area = max(abs_bbox_width * abs_bbox_height, 0)

                area.append(bbox_area)

    # Calculate harmonic mean
    if len(area) > 0:
        harmonic_mean = len(area) / sum(1 / x for x in area)
        print(f"Harmonic Mean of Bounding Box Areas: {harmonic_mean}")
    else:
        print("No bounding box areas found.")

# Example usage
labels_source_path = "path/to/labels"
images_source_path = "path/to/images"
BboxHarmonicMeanCalculator(labels_source_path, images_source_path)
