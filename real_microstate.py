import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame




radius =0.2
# Function to detect particle-particle collisions and update velocities
def detect_particle_collisions():
    for i in range(n_particle):
        for j in range(i + 1, n_particle):
            # Calculate the distance between particles i and j
            dist = np.linalg.norm(particle_position[:, i] - particle_position[:, j])

            # Check if particles are colliding (distance < 2 * radius)
            if dist < 2 * radius:
                # Elastic collision response
                delta_pos = particle_position[:, i] - particle_position[:, j]
                delta_vel = velocities[:, i] - velocities[:, j]
                
                # Velocity update according to elastic collision formula
                factor = np.dot(delta_vel, delta_pos) / np.dot(delta_pos, delta_pos)
                velocities[:, i] -= factor * delta_pos
                velocities[:, j] += factor * delta_pos
                # Play sound effect for particle collision
                pygame.mixer.Sound.play(collision_sound)


# Initialize pygame for sound effects
pygame.mixer.init()
collision_sound = pygame.mixer.Sound('collision.mp3')  # Your sound file

# Number of particles
n_particle = 4

# Set the particle positions randomly within the box
particle_position = np.random.uniform(0, 10, (2, n_particle))
ball_state = np.zeros(5,dtype=int)
particle_in_box = np.zeros((2,n_particle),dtype=int) #note the [0] represent in left and [1] represent right box


update_state = np.zeros((2,n_particle),dtype=int)

# Create random velocities
velocities = np.random.uniform(-1,1,(2, n_particle))
list_micro = np.zeros(16,dtype=int)



plt.style.use('dark_background')
# Create the figure and axis
fig, (ax,ax1) = plt.subplots(nrows=2,ncols=1,figsize=(9,16))
scat = ax.scatter(particle_position[0], particle_position[1], s=50,c=['#ff6666', '#66b3ff', '#99ff99', '#ffcc99'],edgecolor='white', alpha=0.7)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor("black")
# ax.set_facecolor("black")
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.set_title("4-Ideal-Gas Molecules in container parition in 2-Boxes", fontsize=10, fontweight='bold', color='white')
ax.vlines(5,-10,10,colors='white',linestyles="dashed",alpha=0.5)
ax1.set_ylabel("# of microstate occured")
ax1.set_title("Nof Microstate cocured")
ax1.set_xticks(np.linspace(0,17,17,dtype=int))

ax1.set_xlim(0,17)
       

    #[0 0 0 0] #all are in right

    #[1 1 1 1]  #all are in left

    #[1 0 0 0] # one is in left
    #[0 1 0 0]
    #[0 0 1 0]
    #[0 0 0 1]

    #[0 1 1 1] # three in left
    #[1 0 1 1]
    #[1 1 0 1]
    #[1 1 1 0]

    #[1 1 0 0] # two is in left
    #[0 0 1 1]
    #[0 1 1 0]
    #[0 1 0 1]
    #[1 0 1 0]
    #[1 0 0 1]


    #[1 1 1 0]  
    #[0 1 1 1]







# Update function for the animation
def animate(i):
    ax1.clear()
    ax1.set_ylabel("No of Microstates occured", fontsize=10,fontweight='bold', color='white')
    ax1.set_xlabel("Coresponding Microstate", fontsize=10,fontweight='bold', color='white')
    ax1.set_xticks(np.linspace(0,17,17,dtype=int))
    global particle_position ,velocities,update_state,microstate_list
    # Update particle positions
    particle_position += velocities*(1/10)
    particle_in_box = np.zeros((2,n_particle),dtype=int) #note the [0] represent in left and [1] represent right box

    # Check for wall collisions and play sound if collision occurs
    for j in range(n_particle):
        if particle_position[0, j] <= 0 or particle_position[0, j] >= 10:
            velocities[0, j] *= -1  # Reverse x-velocity on collision
            pygame.mixer.Sound.play(collision_sound)  # Play sound on collision

        if particle_position[1, j] <= 0 or particle_position[1, j] >= 10:
            velocities[1, j] *= -1  # Reverse y-velocity on collision
            pygame.mixer.Sound.play(collision_sound)  # Play sound on collision
        #macrotate detection
        #Set of the number of particle in left and right
        if particle_position[0,j] >=5: #this check for right box
            particle_in_box[1,j] +=1
        elif particle_in_box[0,j] <5:
            particle_in_box[0,j] +=1
    detect_particle_collisions()
        #for ploting graph of macrostate
    macrostate =np.zeros(5,dtype=int)
    #[0 1 2 3 4] == [four_left three_left two_two three_right four_right]
    total_macrostate = np.sum(particle_in_box,axis=1,dtype=int)
    # print("no of particle left box",particle_in_box)
    # print(total_macrostate)
    # print(particle_in_box)
    if (particle_in_box == update_state).all():
        pass
    else:

    #[0 0 0 0] #all are in right
    #[1 1 1 1]  #all are in left

    #[1 0 0 0] # one is in left
    #[0 1 0 0]
    #[0 0 1 0]
    #[0 0 0 1]

    #[0 1 1 1] # three in left
    #[1 0 1 1]
    #[1 1 0 1]
    #[1 1 1 0]

    #[1 1 0 0] # two is in left
    #[0 0 1 1]
    #[0 1 1 0]
    #[0 1 0 1]
    #[1 0 1 0]
    #[1 0 0 1]
        list_of_microstate = np.array([
            [1,1, 1, 1],
            [1,1, 1, 0],
            [1,1, 0, 1],
            [1,0, 1, 1],
            [0,1, 1, 1],
            [1,1, 0, 0],
            [0,0, 1, 1],
            [0,1, 1, 0],
            [0,1, 0, 1],
            [1,0, 1, 0],
            [1,0, 0, 1],
            [1,0, 0, 0],
            [0,1, 0, 0],
            [0,0, 1, 0],
            [0,0, 0, 1],
            [0,0, 0, 0]
        ])
        
        
        # print(particle_in_box[0],"that is particle [o, j]")
        for i,list in enumerate(list_of_microstate):
            # print("this is list",list,"with index",i)
            if (particle_in_box[0]==list).all():
                list_micro[i]+=1
                # print("this is_micro",list_micro)
                break
        if total_macrostate[0] ==4: #this is 4 balls in left state
            ball_state[0] +=1
        elif total_macrostate[0] == 3: #3 balls in left
            ball_state[1] +=1
        elif total_macrostate[0] == 2: #2 balls in left
            ball_state[2] +=1
        elif total_macrostate[0] == 1: #3 balls in right
            ball_state[3] +=1
        elif total_macrostate[0] == 0: #4 balls in left
                ball_state[4] +=1
    update_state = particle_in_box
    # print(ball_state)
    # Update scatter plot data
    scat.set_offsets(np.c_[particle_position[0], particle_position[1]])
    # ax1.bar(np.array(["4L","3L","2L&2R","3R","4R"]),ball_state,color=['r','b','y','g','m'])
    # print(microstate_list)atch=['
    ax1.bar(np.linspace(1,17,16,endpoint=False),list_micro,linewidth=0.2,color=['#ff6666', '#66b3ff', '#99ff99', '#ffcc99'], edgecolor='black')
    ax1.grid(color='#cccccc',linestyle='--', linewidth=0.5)
    ax1.set_ylim(0,max(list_micro)+4)
    ax1.set_facecolor('gray')

   

# Run the animation
anim = FuncAnimation(fig , animate, frames=1000,interval=2)



# anim.save('microstate_particle_motion_with_bar1.mp4', writer='ffmpeg', fps=120)

plt.show()
# Quit pygame after the animation ends
pygame.mixer.quit()
