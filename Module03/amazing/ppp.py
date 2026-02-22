from mlx import Mlx


mlx = Mlx()

ptr = mlx.mlx_init()
window = mlx.mlx_new_window(ptr, 600, 600, "1111")

for x in range(600):
    for y in range(600):
        if (x < y):
            mlx.mlx_pixel_put(ptr, window, x, y, 0xFFFFFFFF)


mlx.mlx_loop(ptr)