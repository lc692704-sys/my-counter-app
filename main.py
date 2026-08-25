# Import the main Kivy app class so we can create the app.
from kivy.app import App
# Import the layout class that helps us arrange widgets vertically.
from kivy.uix.boxlayout import BoxLayout
# Import the button widget for the tap button.
from kivy.uix.button import Button
# Import the label widget for showing the number on screen.
from kivy.uix.label import Label


# Define a helper function that increases a number by one.
def increment_count(current: int) -> int:
    # Return the current number plus one.
    return current + 1


# Create a custom widget that acts as the main screen of the app.
class CounterRoot(BoxLayout):
    # Initialize the widget and set up its contents.
    def __init__(self, **kwargs):
        # Call the parent class initializer so the widget works properly.
        super().__init__(**kwargs)
        # Make the layout stack its children vertically from top to bottom.
        self.orientation = "vertical"
        # Add space around the widgets inside the layout.
        self.padding = 24
        # Add space between the widgets.
        self.spacing = 16

        # Start the count at zero.
        self.count = 0
        # Create a label that displays the current count.
        self.label = Label(text="0", font_size="48sp", size_hint_y=None, height=80)
        # Add the label to the layout so it appears on screen.
        self.add_widget(self.label)

        # Create the button the user taps to increase the count.
        self.button = Button(text="Tap to count", font_size="24sp", size_hint_y=None, height=80)
        # Connect the button press event to the increment method.
        self.button.bind(on_press=self.increment)
        # Add the button to the layout so it appears on screen.
        self.add_widget(self.button)

    # Increase the count when the button is pressed.
    def increment(self, instance):
        # Update the count by calling the helper function.
        self.count = increment_count(self.count)
        # Convert the number to text and show it in the label.
        self.label.text = str(self.count)


# Create the main app class that Kivy runs.
class CounterApp(App):
    # Build the app and return the root widget.
    def build(self):
        # Return the main screen widget.
        return CounterRoot()


# Run the app only when this file is executed directly.
if __name__ == "__main__":
    # Start the Kivy application.
    CounterApp().run()
