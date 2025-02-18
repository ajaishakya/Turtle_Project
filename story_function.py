import turtle
import read_story
turtle.speed(0)

# Load the story dictionary
choices = read_story.read_story("story_dictionary.txt")

# Global variables to track used choices and next steps
used_choices = []
next_choices = []

# Initialize turtle screen
screen = turtle.Screen()
screen.title("Interactive Story")
screen.setup(width=800, height=500)

# Create a writer for displaying story text
story_writer = turtle.Turtle()
story_writer.hideturtle()
story_writer.penup()
story_writer.goto(0, 0)

# Button storage
buttons = []

def display_story_text(text):
    """
    Display the story text on the turtle screen.
    """
    story_writer.clear()
    story_writer.write(text, align="center", font=("Arial", 16, "normal"))

#Function to Create Button and writer object
def create_button(label, x, y, choice):
    """
    Create a clickable button for a choice with hover support.
    """
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(x, y)
    button.shape("square")
    button.shapesize(stretch_wid=3, stretch_len=20)
    button.fillcolor("Azure")  # Default button color
    button.onclick(lambda x, y: handle_choice(choice))  # Click event
    button.showturtle()

    # Write the label on the button
    button_writer = turtle.Turtle()
    button_writer.hideturtle()
    button_writer.penup()
    button_writer.goto(x, y - 10)
    button_writer.write(label, align="center", font=("Arial", 12, "bold"))

    return button, button_writer

#Function to quit 
def quit_button():
    """
    This will be added every time new choices are shown.
    """
    x, y = 0, -200
    choice = "Quit"
    label = "Quit"
    button, label_writer = create_button(label, x, y, choice)
    buttons.append((button, label_writer))

def update_buttons():
    """
    Update the buttons and clear old ones before creating new ones.
    """
    # Hide and clear existing buttons and labels
    for button, label_writer in buttons:
        button.hideturtle()
        label_writer.clear()

    buttons.clear()

    # Create new buttons for the current choices
    x, y = -500, -100
    for choice in next_choices:
        if choice == 'Next':
            label = f"{choice}"
            button, label_writer = create_button(label, 0, -100, choice)
            buttons.append((button, label_writer))
            
        else:
            label = f"{choice}"
            button, label_writer = create_button(label, x, y, choice)
            buttons.append((button, label_writer))  # Store both button and writer
            x += 500  # Adjust position for the next button
    
    # Add the quit button every time choices are updated
    quit_button()

def clear_all_buttons():
    """
    Hide and clear all buttons and labels.
    """
    for button, label_writer in buttons:
        button.hideturtle()
        label_writer.clear()
    buttons.clear()

#Function to handle choices
def handle_choice(choice):
    """
    Handle a user's choice and advance the story.
    """
    global next_choices

    # Prevent re-choosing the same option
    if choice in used_choices:
        display_story_text("You've already made that choice. Please choose another option.")
        return

    # Add the choice to used choices
    used_choices.append(choice)

    # Handle quit option separately
    if choice == "Quit":
        clear_all_buttons()
        display_story_text("The End, Hope you enjoyed it !!!")
        return

    # Display the story text for the choice
    display_story_text(choices.get(choice, "This part of the story is not yet written."))

    # Determine the next choices based on user input
    # First Branch
    if choice == 'Explore the room for clues':
        screen.bgpic("A1.gif")
        next_choices = ['Attempt to open the safe.', 'Leave the room and find help.']
    elif choice == 'Attempt to open the safe.':
        screen.bgpic("A11.gif")
        next_choices = ['Next']
    elif choice == 'Leave the room and find help.':
        screen.bgpic("A12.gif")
        next_choices = ['Next']

    #Second Branch
    elif choice == 'Exit through the only open door':
        screen.bgpic("B1.gif")
        next_choices = ['Investigate the screens.', 'Keep walking toward a distant sound.']
    elif choice == 'Investigate the screens.':
        screen.bgpic("B1.gif")
        next_choices = ['Next']
    elif choice == 'Keep walking toward a distant sound.':
        screen.bgpic("B12.gif")
        next_choices = ['Next']

    #Common Ground
    elif choice  == 'Next':
        screen.bgpic("midpoint.gif")
        display_story_text("""
No matter the choices, Sam finds a hidden chamber with a holographic recording of their past self.
Holographic Sam:
"If you're seeing this, it means they've wiped your memory. You were part of Project Echo, and the truth is dangerous. 
Choose wisely: the world depends on it.""")
        next_choices = ['Attempt to restore memories using control panel.', 'Destroy the control panel to prevent tampering.', 'Avoid both actions.']

    #First Branch
    elif choice == 'Attempt to restore memories using control panel.':
        screen.bgpic("A2.gif")
        next_choices = ['Rejoin the resistance', 'Work alone to dismantle the regime']
    elif choice == 'Rejoin the resistance':
        screen.bgpic("A21.gif")
        clear_all_buttons()
        next_choices = []
    elif choice == 'Work alone to dismantle the regime':
        screen.bgpic("A22.gif")
        clear_all_buttons()
        next_choices = []
    
    #Second Branch
    elif choice == 'Destroy the control panel to prevent tampering.':
        screen.bgpic("B2.gif")
        next_choices = ['Seek out the rebellion', 'Disappear into the world']
    elif choice == 'Seek out the rebellion':
        screen.bgpic("B21.gif")
        clear_all_buttons()
        next_choices = []
    elif choice == 'Disappear into the world':
        screen.bgpic("B22.gif")
        clear_all_buttons()
        next_choices = []

    #Third Branch
    elif choice == 'Avoid both actions.':
        screen.bgpic("C2.gif")
        next_choices = ['Embrace freedom and build a new life', 'Investigate remnants of the rebellion']
    elif choice == 'Embrace freedom and build a new life':
        screen.bgpic("C21.gif")
        clear_all_buttons()
        next_choices = []
    elif choice == 'Investigate remnants of the rebellion':
        screen.bgpic("C22.gif")
        clear_all_buttons()
        next_choices = []

    else:
        display_story_text("Invalid choice. Please select a valid option.")

    # Update buttons for the next choices
    update_buttons()

#Programs starting function
def story_function():
    """
    Initialize the story and set up the first choices.
    """
    global next_choices
    screen.bgpic("start.gif")

    display_story_text("""
Title: Echoes of Tomorrow
      
Synopsis :
In a dystopian future dominated by memory manipulation, Sam awakens in a mysterious facility with no recollection of their past. 
As viewers guide Sam through a series of decisions, they uncover the secrets of Project Echo, their pivotal role in a rebellion, 
and the consequences of their actions. Will Sam reclaim their memories, embrace freedom, or shape the world without knowledge 
of their past?

Setting: A dimly lit, metallic room with flickering lights and a warning alarm.
Action: Sam wakes up, disoriented.
      
Sam: (Confused) "Where... am I?"
Narration: "In a world where the past is forgotten, every choice shapes the future."
 \nChoose an action:      
        """)
    next_choices = ['Explore the room for clues', 'Exit through the only open door']
    update_buttons()

turtle.hideturtle()
# Start the story
story_function()

# Start the turtle event loop
screen.mainloop()
