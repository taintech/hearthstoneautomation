import cv2


def find(template_image, search_image):
    image = cv2.imread(search_image, 0)
    template = cv2.imread(template_image, 0)
    w, h = template.shape[::-1]
    method = eval('cv2.TM_CCOEFF_NORMED')
    res = cv2.matchTemplate(image, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return (top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2
