def time(name, task_number, during_time_msec):
    during_time_sec = during_time_msec / 1000

    #print(name + " wykonal(a) zadanie nr " + str(task_number) + " w " + str(during_time_sec) + "s")
    return f"{name} wykonal(a) zadanie nr {task_number} w {during_time_sec:.3f}s"

print(time("Igor", 2, 3500))