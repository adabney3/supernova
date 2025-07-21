# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# class SupernovaSimulation:
#     def __init__(star):
#         star.r_max = 100 #maximum radius
#         star.n_shells = 50 #number of massshells
#         star.dt = 0.1 #time step
#         star.total_time = 5.0 #total time of simulation

#         #radial grid
#         star.r = np.linespace(0.1, star.r_max, star.n_shells)
#         star.initial_r = star.r.copy()

#         star.v = np.zeros_like(star.r) #initial velocities

#         star.core_radius = 10
#         star.shock_position = 0
#         star.time = 0

#         #animation setup
#         star.fig, (star.ax1, star.ax2) = plt.subplots(1, 2, figsize=(12, 5))

#         def gravitational_force(star, r):
#             """simple gravitational acceleration (inward)"""
#             #stronger force for inner regions
#             return -50 / (r**2 + 1)
        
#         def pressure_force(star, r):
#             """pressure force from core bounce and shock"""
#             if star.time > 1.0: #time of core bounce
#                 #shock wave propogation
#                 shock_strength = 100 * np.exp(-(star.time - 1.0))
#                 return shock_strength / (r + 1)
#             return 0
        
#         def update_physics(star):
#             """update positions and velocities"""
#             gravity = np.array([star.gravitational_force(r) for r in star.r])
#             pressure = np.array([star.pressure_force(r) for r in star.r])

#             star.r += np.maximum(star.r, 0.1)

#             if star.time > 1.0:
#                 star.shock_position = 15 + 30 * (star.time - 1.0)

#             star.time += star.dt

#         def get_phase_description(star):
#             """return description of current phase"""
#             if star.time < 1.0:
#                 return "gravitational collapse"
#             elif star.time < 2.0:
#                 return "core bounce"
#             else:
#                 return "shock wave explosion"
            
#         def animate(star, frame):
#             """animation function"""
#             star.ax1.clear()
#             star.ax2.clear()

#             star.update_physics()

#             star.ax1.plot(star.initial_r, star.initial_r, 'b--', alpha = 0.3, label = 'initial')
#             star.ax1.plot(star.initial_r, star.r, 'r--', linewidth = 2, label = 'current')

#             core_mask = star.initial_r <= star.core_radius
#             star.axi.plot(star.initial_r[core_mask], star.r[core_mask], 'ro', markersize = 4)

#             if star.shock_position > 0:
#                 shock_idx = np.argmin(np.abs(star.r - star.shock_position))
#                 star.ax1.plot(star.initial_r[shock_idx], star.r[shock_idx], 'yo', markersize = 8, label = 'shock front')

#             star.ax1.set_xlabel('initial radius')
#             star.ax1.set_ylabel('current radius')
#             star.ax1.set_title(f'stellar structure\ntime: {star.time:.2f}')
#             star.ax1.legend()
#             star.ax1.grid(True, alpha = 0.3)
#             star.ax1.set_xlim(0, star.r_max)
#             star.ax1.set_ylim(0, star.r_max)

#             star.ax2.plot(star.r, star.v, 'g--', linewidth = 2)
#             star.ax2.axhline(y = 0, color = 'k', linestyle = '--', alpha = 0.5)
#             star.ax2.set_xlabel('current radius')
#             star.ax2.set_ylabel('velocity')
#             star.ax2.set_title(f'velocity profile\nphase: {star.get_phase_description()}')
#             star.ax2.grid(True, alpha = 0.3)
#             star.ax2.set_xlim(0, star.r_max)

#             if np.any(star.v > 0):
#                 star.ax2.fill_between(star.r, 0, star.v, where = (star.v > 0), alpha = 0.3, color = 'red', label = 'outflow')
#                 star.ax2.fill_between(star.r, 0, star.v, where = (star.v < 0), alpha = 0.3, color = 'blue', label = 'inflow')

#             star.ax2.legend()

#             plt.tight_layout()

#             if star.time >= star.total_time:
#                 return []
#             return []
#         def run_simulation():
#             """run the supernova simulation"""
#             sim = SupernovaSimulation()

#             frames = int(sim.total_time / sim.dt)
#             anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, interval=50, blit=False, repeat=False)

#             plt.show(block = True)
#             print("simulation complete")

#             return anim
#         if __name__ == "__main__":
#             print("starting core-collapse supernova simulation...")
#             print("phase 1: gravitational collapse (t < 1.0 s)")
#             print("phase 2: core bounce (t = 1.0 s)")
#             print("phase 3: shock wave explosion (t > 1.0 s)")
#             print("\nclose the plot window to end the simulation")

#             try:
#                 print("running simulation...")
#                 anim = run_simulation()
#             except:
#                 print("Animation display failed. Saving as GIF instead...")
#                 # Alternative: save as GIF
#                 sim = SupernovaSimulation()
#                 frames = int(sim.total_time / sim.dt)
#                 anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, 
#                                       interval=50, blit=False, repeat=False)
#                 anim.save('supernova_animation.gif', writer='pillow', fps=20)
#                 print("Animation saved as 'supernova_animation.gif'")




# import numpy as np
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d as Axes3D

# u = np.linspace(0, 2 * np.pi, 50)
# v = np.linspace(0, np.pi, 50)

# radius = 5
# x = radius * np.outer(np.cos(u), np.sin(v))
# y = radius * np.outer(np.sin(u), np.sin(v))
# z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, color='blue', alpha=0.8)

# ax.set_axis_off()

# ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio
# plt.show()

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# # Create sphere coordinates (ultra low resolution for maximum pixelation)
# u = np.linspace(0, 2 * np.pi, 40)
# v = np.linspace(0, np.pi, 30)

# radius = 10
# x = radius * np.outer(np.cos(u), np.sin(v))
# y = radius * np.outer(np.sin(u), np.sin(v))
# z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# # Create 3D plot with black background for retro feel
# fig = plt.figure(figsize=(8, 8), facecolor='black')
# ax = fig.add_subplot(111, projection='3d', facecolor='black')

# # Plot the sphere with ultra pixelated style
# ax.plot_surface(x, y, z, color='magenta', alpha=1.0, linewidth=1, edgecolor='yellow')

# # Remove axes
# ax.set_axis_off()

# # Make it look like a perfect sphere
# ax.set_box_aspect([1,1,1])

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# class SupernovaSimulation:
#     def __init__(self):
#         # Physical parameters
#         self.r_max = 100  # Maximum radius (arbitrary units)
#         self.n_shells = 50  # Number of mass shells
#         self.dt = 0.01  # Time step
#         self.total_time = 5.0  # Total simulation time
        
#         # Initialize radial grid
#         self.r = np.linspace(0.1, self.r_max, self.n_shells)
#         self.initial_r = self.r.copy()
        
#         # Initialize velocities (zero initially)
#         self.v = np.zeros_like(self.r)
        
#         # Stellar parameters
#         self.core_radius = 10  # Core radius
#         self.shock_position = 0  # Shock front position
#         self.time = 0
        
#         # Animation setup
#         self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
#     def gravitational_force(self, r):
#         """Simple gravitational acceleration (inward)"""
#         # Stronger force for inner regions
#         return -50 / (r**2 + 1)
    
#     def pressure_force(self, r):
#         """Pressure force from core bounce and shock"""
#         if self.time > 1.0:  # Core bounce happens at t=1
#             # Shock wave propagation
#             shock_strength = 100 * np.exp(-(self.time - 1.0))
#             if r < self.shock_position:
#                 return shock_strength / (r + 1)
#         return 0
    
#     def update_physics(self):
#         """Update positions and velocities"""
#         # Calculate forces
#         gravity = np.array([self.gravitational_force(r) for r in self.r])
#         pressure = np.array([self.pressure_force(r) for r in self.r])
        
#         # Update velocities (F = ma, assuming unit mass)
#         self.v += (gravity + pressure) * self.dt
        
#         # Update positions
#         self.r += self.v * self.dt
        
#         # Prevent shells from going to zero radius
#         self.r = np.maximum(self.r, 0.1)
        
#         # Update shock position after core bounce
#         if self.time > 1.0:
#             self.shock_position = 15 + 30 * (self.time - 1.0)
        
#         self.time += self.dt
    
#     def get_phase_description(self):
#         """Return description of current phase"""
#         if self.time < 1.0:
#             return "Gravitational Collapse"
#         elif self.time < 2.0:
#             return "Core Bounce"
#         else:
#             return "Shock Wave Explosion"
    
#     def animate(self, frame):
#         """Animation function"""
#         # Clear axes
#         self.ax1.clear()
#         self.ax2.clear()
        
#         # Update physics
#         self.update_physics()
        
#         # Plot 1: Radial structure
#         self.ax1.plot(self.initial_r, self.initial_r, 'b--', alpha=0.3, label='Initial')
#         self.ax1.plot(self.initial_r, self.r, 'r-', linewidth=2, label='Current')
        
#         # Mark core region
#         core_mask = self.initial_r <= self.core_radius
#         self.ax1.plot(self.initial_r[core_mask], self.r[core_mask], 'ro', markersize=4)
        
#         # Mark shock front
#         if self.shock_position > 0:
#             shock_idx = np.argmin(np.abs(self.r - self.shock_position))
#             self.ax1.plot(self.initial_r[shock_idx], self.r[shock_idx], 'yo', 
#                          markersize=8, label='Shock Front')
        
#         self.ax1.set_xlabel('Initial Radius')
#         self.ax1.set_ylabel('Current Radius')
#         self.ax1.set_title(f'Stellar Structure\nTime: {self.time:.2f}')
#         self.ax1.legend()
#         self.ax1.grid(True, alpha=0.3)
#         self.ax1.set_xlim(0, self.r_max)
#         self.ax1.set_ylim(0, self.r_max)
        
#         # Plot 2: Velocity profile
#         self.ax2.plot(self.r, self.v, 'g-', linewidth=2)
#         self.ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5)
#         self.ax2.set_xlabel('Current Radius')
#         self.ax2.set_ylabel('Velocity')
#         self.ax2.set_title(f'Velocity Profile\nPhase: {self.get_phase_description()}')
#         self.ax2.grid(True, alpha=0.3)
#         self.ax2.set_xlim(0, self.r_max)
        
#         # Color-code velocity regions
#         if np.any(self.v > 0):
#             self.ax2.fill_between(self.r, 0, self.v, where=(self.v > 0), 
#                                  alpha=0.3, color='red', label='Outflow')
#         if np.any(self.v < 0):
#             self.ax2.fill_between(self.r, 0, self.v, where=(self.v < 0), 
#                                  alpha=0.3, color='blue', label='Inflow')
        
#         self.ax2.legend()
        
#         plt.tight_layout()
        
#         # Stop animation when time exceeds total time
#         if self.time >= self.total_time:
#             return []
        
#         return []

# def run_simulation():
#     """Run the supernova simulation"""
#     sim = SupernovaSimulation()
    
#     # Create animation
#     frames = int(sim.total_time / sim.dt)
#     anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, 
#                                   interval=50, blit=False, repeat=False)
    
#     # Keep the animation object alive
#     plt.show(block=True)
    
#     return anim

# # Run the simulation
# if __name__ == "__main__":
#     print("Starting Core-Collapse Supernova Simulation...")
#     print("Phase 1: Gravitational collapse (t < 1.0)")
#     print("Phase 2: Core bounce (t = 1.0)")
#     print("Phase 3: Shock wave explosion (t > 1.0)")
#     print("\nClose the plot window to end the simulation.")
    
#     # Try to show animation
#     try:
#         anim = run_simulation()
#     except:
#         print("Animation display failed. Saving as GIF instead...")
#         # Alternative: save as GIF
#         sim = SupernovaSimulation()
#         frames = int(sim.total_time / sim.dt)
#         anim = animation.FuncAnimation(sim.fig, sim.animate, frames=frames, 
#                                       interval=50, blit=False, repeat=False)
#         anim.save('supernova_animation.gif', writer='pillow', fps=20)
#         print("Animation saved as 'supernova_animation.gif'")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

class SupernovaStar:
    def __init__(self):
        # Time parameters
        self.dt = 0.05
        self.time = 0
        self.total_time = 8.0
        
        # Star structure (concentric shells)
        self.n_shells = 20
        self.initial_radii = np.linspace(0.3, 3.0, self.n_shells)  # From core to surface
        self.current_radii = self.initial_radii.copy()
        self.velocities = np.zeros(self.n_shells)
        
        # Colors for different layers (core=red, outer=yellow/white)
        self.colors = plt.cm.hot(np.linspace(0.3, 1.0, self.n_shells))
        
        # Physics parameters
        self.core_bounce_time = 2.0
        self.explosion_start = 2.5
        self.shock_wave_speed = 0.8
        self.shock_position = 0
        
        # Create 3D plot
        self.fig = plt.figure(figsize=(12, 6))
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)
        
    def get_phase(self):
        """Return current phase of supernova"""
        if self.time < self.core_bounce_time:
            return "Gravitational Collapse", "red"
        elif self.time < self.explosion_start:
            return "Core Bounce", "orange"
        else:
            return "Supernova Explosion", "yellow"
    
    def update_physics(self):
        """Update the physics of each shell"""
        phase, _ = self.get_phase()
        
        if phase == "Gravitational Collapse":
            # Inward collapse - stronger for outer shells
            for i in range(self.n_shells):
                gravity_strength = 0.5 * (1 + i/self.n_shells)
                self.velocities[i] -= gravity_strength * self.dt
                
        elif phase == "Core Bounce":
            # Core stops collapsing, starts bouncing
            bounce_strength = 2.0 * np.exp(-(self.time - self.core_bounce_time))
            for i in range(self.n_shells):
                if i < self.n_shells // 3:  # Inner core
                    self.velocities[i] = bounce_strength * (1 - i/self.n_shells)
                    
        else:  # Explosion phase
            # Shock wave propagates outward
            self.shock_position = self.shock_wave_speed * (self.time - self.explosion_start)
            
            for i in range(self.n_shells):
                current_r = self.initial_radii[i]
                if current_r < self.shock_position:
                    # Shell hit by shock wave - accelerate outward
                    explosion_force = 3.0 * np.exp(-(self.time - self.explosion_start) * 0.5)
                    self.velocities[i] = max(self.velocities[i], explosion_force)
        
        # Update positions
        self.current_radii += self.velocities * self.dt
        
        # Prevent shells from going negative or crossing each other
        self.current_radii = np.maximum(self.current_radii, 0.1)
        for i in range(1, self.n_shells):
            if self.current_radii[i] < self.current_radii[i-1]:
                self.current_radii[i] = self.current_radii[i-1] + 0.1
        
        self.time += self.dt
    
    def create_sphere(self, radius, color, alpha=0.6):
        """Create a 3D sphere"""
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = radius * np.outer(np.cos(u), np.sin(v))
        y = radius * np.outer(np.sin(u), np.sin(v))
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
        return x, y, z
    
    def animate(self, frame):
        """Animation function"""
        # Clear the 3D plot
        self.ax1.clear()
        self.ax2.clear()
        
        # Update physics
        self.update_physics()
        
        # Get current phase
        phase, phase_color = self.get_phase()
        
        # Plot 3D star
        self.ax1.set_xlim(-4, 4)
        self.ax1.set_ylim(-4, 4)
        self.ax1.set_zlim(-4, 4)
        
        # Draw each shell as a transparent sphere
        for i in range(self.n_shells-1, -1, -1):  # Draw from outside to inside
            radius = self.current_radii[i]
            color = self.colors[i]
            
            # Adjust alpha based on phase
            if phase == "Supernova Explosion":
                alpha = 0.8 if i < self.n_shells//2 else 0.4
            else:
                alpha = 0.7 if i < self.n_shells//2 else 0.3
            
            # Create and plot sphere
            if radius > 0.1:
                x, y, z = self.create_sphere(radius, color, alpha)
                self.ax1.plot_surface(x, y, z, color=color, alpha=alpha, 
                                    linewidth=0, antialiased=True)
        
        # Add shock wave visualization
        if phase == "Supernova Explosion" and self.shock_position > 0:
            if self.shock_position < 4:
                x, y, z = self.create_sphere(self.shock_position, 'cyan', 0.2)
                self.ax1.plot_surface(x, y, z, color='cyan', alpha=0.3, 
                                    linewidth=1, antialiased=True)
        
        self.ax1.set_title(f'3D Star View\n{phase}\nTime: {self.time:.2f}s', 
                          color=phase_color, fontsize=12, fontweight='bold')
        self.ax1.set_xlabel('X')
        self.ax1.set_ylabel('Y')
        self.ax1.set_zlabel('Z')
        
        # Plot radius vs time (2D view)
        time_points = np.linspace(0, self.time, max(1, int(self.time/self.dt)))
        
        # Show a few key shells
        key_shells = [0, self.n_shells//3, 2*self.n_shells//3, self.n_shells-1]
        labels = ['Core', 'Inner', 'Middle', 'Surface']
        colors_2d = ['red', 'orange', 'yellow', 'white']
        
        for i, (shell_idx, label, color) in enumerate(zip(key_shells, labels, colors_2d)):
            self.ax2.plot(self.time, self.current_radii[shell_idx], 'o', 
                         color=color, markersize=8, label=label)
        
        # Show initial radii as reference
        for i, shell_idx in enumerate(key_shells):
            self.ax2.axhline(y=self.initial_radii[shell_idx], color=colors_2d[i], 
                           linestyle='--', alpha=0.5)
        
        self.ax2.set_xlim(0, self.total_time)
        self.ax2.set_ylim(0, 6)
        self.ax2.set_xlabel('Time (s)')
        self.ax2.set_ylabel('Radius')
        self.ax2.set_title('Shell Radii Over Time')
        self.ax2.legend()
        self.ax2.grid(True, alpha=0.3)
        
        # Add phase annotations
        self.ax2.axvline(x=self.core_bounce_time, color='orange', linestyle=':', alpha=0.7, label='Core Bounce')
        self.ax2.axvline(x=self.explosion_start, color='red', linestyle=':', alpha=0.7, label='Explosion Start')
        
        plt.tight_layout()
        
        # Stop when time exceeds total time
        return self.time < self.total_time

def run_simulation():
    """Run the supernova simulation"""
    print("3D Supernova Simulation Starting...")
    print("Phase 1: Gravitational Collapse")
    print("Phase 2: Core Bounce") 
    print("Phase 3: Supernova Explosion")
    print("\nWatch the 3D star on the left!")
    
    star = SupernovaStar()
    
    # Create animation
    frames = int(star.total_time / star.dt)
    anim = animation.FuncAnimation(star.fig, star.animate, frames=frames,
                                  interval=100, blit=False, repeat=True)
    
    plt.show()
    return anim

# Run the simulation
if __name__ == "__main__":
    anim = run_simulation()