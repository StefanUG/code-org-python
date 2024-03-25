import turtle

# Define the coordinates for the bee shape (a simple polygon)
bee_shape = (
    (-4, 0),   
    (-3, -1),   
    (-1.9, -1.5),  
    (-0.8, -1.5), 
    (1.9, -0.5), # Start of top wing
    (-1.8, -2.7), 
    (-2.1, -3.5), 
    (-1.9, -4.3), 
    (-1.9, -4.3)
)

lg_bee_shape = (
    (-22, 0),   
    (-20, -4),   
    (-13, -7),  
    (-5.6, -7.6), 
    (7.4, -2.6), # Start of top wing
    (-10.5, -13.1), 
    (-13, -18), 
    (-11, -23), 
    (-6, -25), 
    (-1, -23), 
    (7.5, -2.6), # End of top wing
    (9, -7), 
    (15, -6), 
    (17, -4), # Start of top antenna
    (20, -7), 
    (22, -11),  # Tip of top antenna
    (20, -7), 
    (17, -4), # End of top antenna
    (18, 0), 
    (17, 4), # Start of bottom antenna
    (20, 7), 
    (22, 11), # Tip of bottom antenna
    (20, 7),
    (17, 4), # End of bottom antenna
    (15, 6),
    (9, 7), 
    (7.5, 2.6), # Start of bottom wing
    (-1, 23), 
    (-6, 25), 
    (-11, 23), 
    (-13, 18), 
    (-10.5, 13.1), 
    (7.4, 2.6), # End of bottom wing
    (-5.6, 7.6), 
    (-13, 7),  
    (-20, 4)
#    (-22, 0),   
)


lg_bee_shape2 = (
    (0    , -22   ),   
    (-4   , -20   ),   
    (-7   , -13   ),  
    (-7.6 , -5.6  ), 
    (-2.6 , 7.4   ), # Start of top wing
    (-13.1, -10.5 ), 
    (-18  , -13   ), 
    (-23  , -11   ), 
    (-25  , -6    ), 
    (-23  , -1    ), 
    (-2.6 , 7.5   ), # End of top wing
    (-7   , 9     ), 
    (-6   , 15    ), 
    (-4   , 17    ), # Start of top antenna
    (-7   , 20    ), 
    (-11  , 22    ),  # Tip of top antenna
    (-7   , 20    ), 
    (-4   , 17    ), # End of top antenna
    (0    , 18    ), 
    (4    , 17    ), # Start of bottom antenna
    (7    , 20    ), 
    (11   , 22    ), # Tip of bottom antenna
    (7    , 20    ),
    (4    , 17    ), # End of bottom antenna
    (6    , 15    ),
    (7    , 9     ), 
    (2.6  , 7.5   ), # Start of bottom wing
    (23   , -1    ), 
    (25   , -6    ), 
    (23   , -11   ), 
    (18   , -13   ), 
    (13.1 , -10.5 ), 
    (2.6  , 7.4   ), # End of bottom wing
    (7.6  , -5.6  ), 
    (7    , -13   ),  
    (4    , -20   )
)


# Register the bee shape with the name "bee"
turtle.register_shape("bee", lg_bee_shape2)

# Create a turtle using our custom bee shape
bee_turtle = turtle.Turtle()
bee_turtle.shape("bee")
bee_turtle.fillcolor("yellow")  # Optional: Fill the bee shape with color

# Move the bee forward (you can add more movements here)
for i in range(50):
    bee_turtle.forward(5 + 2 * i)
    bee_turtle.right(45)

# Keep the turtle window open
turtle.done()
