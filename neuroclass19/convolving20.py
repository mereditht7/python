# ------------------------------------------------------------
# 1) Synthetic 100×100 white-square image
# ------------------------------------------------------------
def make_synthetic_image():
    img = [[0.0 for _ in range(100)] for _ in range(100)]
    for i in range(30, 70):          # rows 30-69
        for j in range(30, 70):      # cols 30-69
            img[i][j] = 255.0
    return img

def make_circle_image():
    img = [[0.0 for _ in range(100)] for _ in range(100)]
    cx, cy, r = 50, 50, 20                       # centre (50,50), radius 20
    for i in range(100):
        for j in range(100):
            if (i - cy) ** 2 + (j - cx) ** 2 <= r ** 2:
                img[i][j] = 255.0               # inside circle → white
    return img

# ------------------------------------------------------------
# 2) Plain 2-D convolution (no numpy helpers)
# ------------------------------------------------------------
def convolve2d_plain(image, kernel):
    #code here
    """
    Performs a 2D convolution on an input matrix with a given kernel.

    Args:
        input_matrix (list of lists): The 2D input matrix.
        kernel (list of lists): The 2D convolution kernel.

    Returns:
        list of lists: The convolved output matrix.
    """

    input_height = len(image)
    input_width = len(image[0]) if input_height > 0 else 0
    kernel_height = len(kernel)
    kernel_width = len(kernel[0]) if kernel_height > 0 else 0

    # Calculate output dimensions
    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1

    if output_height <= 0 or output_width <= 0:
        return [] # Return empty if no valid convolution can be performed

    result = [[0.0 for _ in range(output_width)] for _ in range(output_height)]

    # Flip the kernel for convolution (important for true convolution)
    flipped_kernel = [row[::-1] for row in kernel[::-1]] 

    for i in range(output_height):
        for j in range(output_width):
            # Calculate the sum of products for the current window
            current_sum = 0.0
            for k_row in range(kernel_height):
                for k_col in range(kernel_width):
                    current_sum += (
                        image[i + k_row][j + k_col] * flipped_kernel[k_row][k_col]
                    )
            result[i][j] = current_sum

    return result

    # output image (same size) filled with zeros
    #result = 0

    # slide kernel over every pixel
        #code here
    #return result

# ------------------------------------------------------------
# 3) Sobel kernels
# ------------------------------------------------------------
sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]
sobel_y = [
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
]

# ------------------------------------------------------------
# 4) Run everything
# ------------------------------------------------------------
img      = make_circle_image()
grad_x   = convolve2d_plain(img, sobel_x)   # vertical edges
grad_y   = convolve2d_plain(img, sobel_y)   # horizontal edges




import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 5) Print full matrices (will be big!)
# ------------------------------------------------------------
import sys
sys.setrecursionlimit(10000)                # allow huge prints

print("=== Raw brightness matrix (img) ===")
for row in img:
    print(row)

print("\n=== Sobel-x (vertical edges) grad_x ===")
for row in grad_x:
    print(row)

print("\n=== Sobel-y (horizontal edges) grad_y ===")
for row in grad_y:
    print(row)

plt.imshow(grad_x, cmap='gray')
plt.show()

plt.imshow(grad_y, cmap='gray')
plt.show()