def jpg2png():
#     global chars
#     str = "abcdefghijklmnopqrstuvwxyz"
#     for i in str:
#         new = JpgimgPath/f'{i}.jpg'
#         img = Image.open(new).convert("L")

#         gray = np.array(img)
#         thresh = threshold_otsu(gray)
#         mask = gray < thresh

#         rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
#         rgba[..., 0] = gray        # Red
#         rgba[..., 1] = gray        # Green 
#         rgba[..., 2] = gray        # Blue 
#         rgba[..., 3] = mask * 255  #transparent