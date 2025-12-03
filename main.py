# ==== main.py ====
import numpy as np
import matplotlib.pyplot as plt

def simulate(m, k, c, x0, v0, t_max, dt):
    n = int(t_max / dt) + 1
    t = np.linspace(0, t_max, n)
    x = np.empty(n)
    v = np.empty(n)
    x[0] = x0
    v[0] = v0
    for i in range(1, n):
        a = -(c / m) * v[i - 1] - (k / m) * x[i - 1]
        v[i] = v[i - 1] + a * dt
        x[i] = x[i - 1] + v[i - 1] * dt
    return t, x, v

def main():
    m = 1.0
    k = 1.0
    c_vals = {
        "Underdamped": 0.5,
        "Critically damped": 2.0,
        "Overdamped": 5.0
    }
    x0 = 1.0
    v0 = 0.0
    t_max = 20.0
    dt = 0.01

    results = {}
    for label, c in c_vals.items():
        t, x, v = simulate(m, k, c, x0, v0, t_max, dt)
        results[label] = (t, x, v)

    # Displacement vs time plot
    plt.figure()
    for label, (t, x, _) in results.items():
        plt.plot(t, x, label=label)
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Displacement vs Time for Different Damping Regimes')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('displacement_vs_time.png')
    plt.close()

    # Phase-space plot
    plt.figure()
    for label, (_, x, v) in results.items():
        plt.plot(x, v, label=label)
    plt.xlabel('Displacement (m)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Phase Space Trajectories')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('phase_space.png')
    plt.close()

    # Primary numeric answer: critical damping coefficient
    c_crit = 2 * np.sqrt(k * m)
    print('Answer:', c_crit)

if __name__ == '__main__':
    main()

