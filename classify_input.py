import csv
import os

legend = []

labels_dir = "all_images/images/data/legend.csv"
with open(labels_dir, 'r') as csvfile:
    legend_reader = csv.reader(csvfile)
    headers = next(legend_reader)
    for row in legend_reader:
        user_id = row[0]
        image_name = row[1]
        emotion = row[2]
        legend.append((image_name, emotion))

src_img_dir = "all_images/images/images/"
dst_img_dir = "images/"
num_missing_files = 0
num_added_files = 0
num_existing_files = 0
num_emotions_added = 0
for entry in legend:
    filename = entry[0]
    emotion = entry[1].lower()
    exists = os.path.isfile(src_img_dir+filename)
    if exists:
        # create a new directory for this classification if one doesn't already exist
        new_dir = dst_img_dir + emotion
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            num_emotions_added += 1
        if not os.path.isfile(dst_img_dir + emotion + "/" + filename):
            os.rename(src_img_dir + filename, dst_img_dir + emotion + "/" + filename)
            num_added_files += 1
        else:
            num_existing_files += 1
    else:
        # Not all entries in legend.csv exist as files
        num_missing_files += 1


print(len(legend))
print(num_missing_files)
# img_dir = "images/images/"
#
# for entry in legend:
#     print(entry[0])
#     print(entry[1])
#     img = cv2.imread(img_dir + entry[0])
#     res = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)
#     print(len(res))
#     break
