import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SupernovaSimulation:
    def __init__(star):
        star.r_max = 100 #maximum radius
        star.n_shells = 50 #number of massshells
        star.dt = 0.1 #time step
        star.total_time = 5.0 #total time of simulation

        #radial grid
        star.r = np.linespace(0.1, star.r_max, star.n_shells)
        star.initial_r = star.r.copy()

        star.v = np.zeros_like(star.r) #initial velocities

        star.core_radius = 10
        star.shock_position = 0
        star.time = 0

        #animation setup
        star.fig, (star.ax1, star.ax2) = plt.subplots(1, 2, figsize=(12, 5))

        def gravitational_force(star, r):
            """simple gravitational acceleration (inward)"""
            #stronger force for inner regions
            return -50 / (r**2 + 1)
        
        def pressure_force(star, r):
            """pressure force from core bounce and shock"""
            if star.time > 1.0: #time of core bounce
                #shock wave propogation
                shock_strength = 100 * np.exp(-(star.time - 1.0))
                return shock_strength / (r + 1)
            return 0
        
        def update_physics(star):
            """update positions and velocities"""
            gravity = np.array([star.gravitational_force(r) for r in star.r])
            pressure = np.array([star.pressure_force(r) for r in star.r])

            star.r += np.maximum(star.r, 0.1)

            if star.time > 1.0:
                star.shock_position = 15 + 30 * (star.time - 1.0)

            star.time += star.dt

        def get_phase_description(star):
            """return description of current phase"""
            if star.time < 1.0:
                return "gravitational collapse"
            elif star.time < 2.0:
                return "core bounce"
            else:
                return "shock wave explosion"
            
        def animate(star, frame):
            """animation function"""
            star.ax1.clear()
            star.ax2.clear()

            star.update_physics()

            star.ax1.plot(star.initial_r, star.initial_r, 'b--', alpha = 0.3, label = 'initial')
            star.ax1.plot(star.initial_r, star.r, 'r--', linewidth = 2, label = 'current')

            core_mask = star.initial_r <= star.core_radius
            star.axi.plot(star.initial_r[core_mask], star.r[core_mask], 'ro', markersize = 4)

            if star.shock_position > 0:
                shock_idx = np.argmin(np.abs(star.r - star.shock_position))
                star.ax1.plot(star.initial_r[shock_idx], star.r[shock_idx], 'yo', markersize = 8, label = 'shock front')

            star.ax1.set_xlabel('initial radius')
            star.ax1.set_ylabel('current radius')
            star.ax1.set_title(f'stellar structure\ntime: {star.time:.2f}')
            star.ax1.legend()
            star.ax1.grid(True, alpha = 0.3)
            star.ax1.set_xlim(0, star.r_max)
            star.ax1.set_ylim(0, star.r_max)

            star.ax2.plot(star.r, star.v, 'g--', linewidth = 2)
            star.ax2.axhline(y = 0, color = 'k', linestyle = '--', alpha = 0.5)
            star.ax2.set_xlabel('current radius')
            star.ax2.set_ylabel('velocity')
            star.ax2.set_title(f'velocity profile\nphase: {star.get_phase_description()}')
            star.ax2.grid(True, alpha = 0.3)
            star.ax2.set_xlim(0, star.r_max)

            if np.any(star.v > 0):
                star.ax2.fill_between(star.r, 0, star.v, where = (star.v > 0), alpha = 0.3, color = 'red', label = 'outflow')
                star.ax2.fill_between(star.r, 0, star.v, where = (star.v < 0), alpha = 0.3, color = 'blue', label = 'inflow')

            star.ax2.legend()

            plt.tight_layout()

            if star.time >= star.total_time:
                return []
            return []
        def run_simulation():
            """run the supernova simulation"""
            sim = SupernovaSimulation()

            frames = int(sim.total_time / sim.dt)
            anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, interval=50, blit=False, repeat=False)

            plt.show(block = True)
            print("simulation complete")

            return anim
        if __name__ == "__main__":
            print("starting core-collapse supernova simulation...")
            print("phase 1: gravitational collapse (t < 1.0 s)")
            print("phase 2: core bounce (t = 1.0 s)")
            print("phase 3: shock wave explosion (t > 1.0 s)")
            print("\nclose the plot window to end the simulation")

            try:
                print("running simulation...")
                anim = run_simulation()
            except:
                print("Animation display failed. Saving as GIF instead...")
                # Alternative: save as GIF
                sim = SupernovaSimulation()
                frames = int(sim.total_time / sim.dt)
                anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, 
                                      interval=50, blit=False, repeat=False)
                anim.save('supernova_animation.gif', writer='pillow', fps=20)
                print("Animation saved as 'supernova_animation.gif'")
