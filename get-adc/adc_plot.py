from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(left = 0)
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(len(time)-1):
        sampling_periods.append(time[i+1] - time[i])
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title("Гистограмма времени измерения")
    plt.xlabel("Время, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()