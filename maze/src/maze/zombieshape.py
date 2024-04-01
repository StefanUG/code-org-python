import turtle

zombie_shape = (
    (-15    , 0   ),   
    (-13   , -5   ),   # return to here
    (-8   , -9   ),  
    ( 0   , -9   ),  
    ( 5   , -7   ),  
    ( 0   , -9   ), 
    (-8   , -9   ), 
    (-13  , -5   ),  # done
    (-12 , -15   ),  
    (-9  , -19    ), 
    (0  , -19   ), 
    (9  , -16   ), # ret
    (5  , -7    ), 
    (9  , -16    ), # done
    (13   , -15     ), 
    (13   , -9    ), 
    (11   , -7    ), 
    (5   , -7    ), 
    (8  , 0    ),  # half way, now mirror

    (5   , 7    ), 
    (11   , 7    ), 
    (13   , 9    ), 
    (13   , 15     ), 
    (9  , 16    ), # done
    (5  , 7    ), 
    (9  , 16   ), # ret
    (0  , 19   ), 
    (-9  , 19    ), 
    (-12 , 15   ),  
    (-13  , 5   ),  # done
    (-8   , 9   ), 
    ( 0   , 9   ), 
    ( 5   , 7   ),  
    ( 0   , 9   ),  
    (-8   , 9   ),  
    (-13   , 5   ), 
    (-15    , 0   ),   



)



zombie_shape_2 = (
    ( 0  , -15  ),   
    ( -5 , -13  ),   # return to here
    ( -9 , -8   ),  
    ( -9 ,  0   ),  
    ( -7 ,  5   ),  
    ( -9 ,  0   ), 
    ( -9 , -8   ), 
    ( -5 , -13  ),  # done
    ( -15, -12  ),  
    ( -19, -9   ), 
    ( -19, 0    ), 
    ( -16, 9    ), # ret
    ( -7 , 5    ), 
    ( -16, 9    ), # done
    ( -15, 13   ), 
    ( -9 , 13   ), 
    ( -7 , 11   ), 
    ( -7 , 5    ), 
    ( 0  , 8    ),  # half way, now mirror
    ( 7  , 5    ), 
    ( 7  , 11   ), 
    ( 9  , 13   ), 
    ( 15 , 13   ), 
    ( 16 , 9    ), # done
    ( 7  , 5    ), 
    ( 16 , 9    ), # ret
    ( 19 , 0    ), 
    ( 19 , -9   ), 
    ( 15 , -12  ),  
    ( 5  , -13  ),  # done
    ( 9  , -8   ), 
    ( 9  ,  0   ), 
    ( 7  ,  5   ),  
    ( 9  ,  0   ),  
    ( 9  , -8   ),  
    ( 5  , -13  ), 
    ( 0  , -15  ),   

)



turtle.register_shape("zombie", zombie_shape_2)

zombie = turtle.Turtle()
zombie.shape("zombie")
zombie.color("brown", "green")

zombie.forward(100)

# # Move the bee forward (you can add more movements here)
# for i in range(50):
#     zombie.forward(5 + 2 * i)
#     zombie.right(45)



# Keep the turtle window open
turtle.done()
