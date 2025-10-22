import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("NEWPAGE.png")

# --- 1️⃣ Convert to HSV (better color filtering than grayscale) ---
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# --- 2️⃣ Reduce red/pink tones (high H ~0-20, high S) ---
# This removes the margin line color before grayscale
red_mask = ((h < 20) | (h > 160)) & (s > 70)
v[red_mask] = 255  # make red/pink zones white → ignored

# --- 3️⃣ Convert to grayscale (use modified value channel) ---
gray = v

# --- 4️⃣ Remove top and left margin zones ---
h, w = gray.shape
gray[:int(h*0.1), :] = 255     # top 10% = white
gray[:, :int(w*0.1)] = 255     # left 10% = white

# --- 5️⃣ Adaptive threshold + morphological cleanup ---
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY_INV, 25, 15
)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))
morph = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# --- 6️⃣ Horizontal projection profile ---
horizontal_sum = np.sum(morph, axis=1)
threshold = np.max(horizontal_sum) * 0.3
line_indices = np.where(horizontal_sum > threshold)[0]

# --- 7️⃣ Group nearby y-values ---
lines_y = []
group = [line_indices[0]]
for i in range(1, len(line_indices)):
    if line_indices[i] - line_indices[i-1] > 5:
        lines_y.append(int(np.mean(group)))
        group = []
    group.append(line_indices[i])
if group:
    lines_y.append(int(np.mean(group)))

print("Detected lines:", lines_y)

# --- 8️⃣ Visualization ---
vis = img.copy()
for y in lines_y:
    cv2.line(vis, (0, y), (w, y), (0, 255, 0), 1)

plt.imshow(cv2.cvtColor(vis, cv2.COLOR_BGR2RGB))
plt.title("Clean Line Detection (No Margins, Any Color)")
plt.show()
