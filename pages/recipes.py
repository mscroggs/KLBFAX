from page import Page

class RecipePage(Page):
    def __init__(self, n, title, recipe):
        super(RecipePage, self).__init__(n)
        self.title = title
        self.in_index=False
        self.recipe = recipe

    def generate_content(self):
        self.add_title(self.title)
        self.add_wrapped_text(self.recipe, pre=4)


r1 = RecipePage("691","Bad Tempered Cake","""
  1/2 lb    Rich tea and/or digestive biscuits
    4 oz    Margarine
    1 dsp   Sugar
    3 dsp   Cocoa
    3 dsp   Drinking chocolate
1 1/2 tbsp  Golden syrup
    2 oz    Sultanas
    2 bars  Milk chocolate

1. Break the biscuits.
2. Melt the margarine, sugar, cocoa, drinking chocolate and syrup over a medium heat.
3. Mix with biscuits and sultanas and press down in baking tray.
4. Cover with melted milk chocolate.
5. Leave in the fridge to set""")

r2 = RecipePage("692","Huda Friendship Cake","""
Day 1:    Put me in a large mixing bowl and cover loosely with a tea towel.
Days 2-3: Stir well.
Day 4:    HUDA HUNGRY. Add 1 cup each of plain flour, sugar and milk. Stir well.
Days 5-8: Stir well.
Day 9:    Add the same as day 4 and stir well. Divide into 4 equal portions and give away to friends with a copy of these instructions. Keep the fourth portion.
Day 10:   Now you are ready to make the cake. Stir well and add the following:
    1 cup of sugar (8oz or 225g)     2 cups plain flour (10oz or 300g)
    half tsp. salt                   2/3 cup of cooking oil (5.3oz or 160ml)
    2 eggs                           2 tsp. vanilla essence
    2 cooking apples cut into chunks 1 cup raisins (7oz or 200g)
    2 heaped tsp. cinnamon           2 heaped tsp. baking powder
    Optional: 1/4 cup brown sugar    Optional: 1/4 cup melted butter
    Mix everything together and put into a large greased baking tin. Sprinkle with a quarter of a cup of brown sugar and a quarter of a cup of melted butter. Bake for 45 minutes at 170-180C. Test the middle with a clean knife; you may need to cover in tin foil and bake for a further 20 minutes to make sure Huda is cooked properly in the middle. When baked, Huda can be frozen.
""")

r3 = RecipePage("693","Kvass",
"""
    2 L     Water
    100g    Sugar
    7g      Yeast
    6 slices of Bread

1. Toast bread until super-brown (or burnt!)
2. Boil the water in a kettle
3. Put the burnt bread and boiled water in a pan.
4. Leave for 5-10 minutes ot until the water is tea-coloured.
5. Take the bread out the pan and put in a sieve above the pan. Squeeze out any water from the soggy bread.
6. Discard the bread.
7. Stir in the sugar, then the yeast.
8. Transfer to a glass bottle and leave out in the sun for half a day.

Note: The longer you leave the kvass out, the better. Three days is perfect!

""")

r4 = RecipePage("694","Pesto Twists",
"""
    1 sheet Puff pastry (all butter)
    100g    Soft cheese
    100g    Pesto (see page 695)
    1       Egg (yolk only)

1. Cut pastry sheet in half.
2. Spread soft cheese on one half.
3. Spread pesto on the cheese.
4. Cover with the other half of pastry (like a sandwich).
5. Cut into 1cm wide, 6cm long strips. Twist and place on a baking tray.
6. Bake in the oven for 20 minutes at 180"""+u"\u00b0"+"C")

r5 = RecipePage("695","Pesto",
"""
    100g    Pine nuts
    100g    Parmesan cheese
    50g     Olive oil
    4 cloves of Garlic
    One large basil plant (or two small basil plants)

1. Put in blender.
2. Turn on blender.
3. Wait.
4. Turn off blender.
5. Hey Pesto!

    Note: You can make other kinds of pesto if you replace the basil with another ingredient, such as rocket, mint or sundried tomatoes. In fact, if you put straw rather than basil leaves, you end up with HEY PESTO!""")

r6 = RecipePage("696","Chalkdust Rocky Road","""
INGREDIENTS

    300g    Marshmallows
    300g    Chocolate
    100g    Butter
    80g     Youghurt + cream
    50g     Hazelnuts
    50g     Walnuts
    50g     Pistachio nuts
    50g     Blanched almonds
    50g     Sunflower seeds
    
    Turn to Page 697 for the method.
""")

r7 = RecipePage("697","Chalkdust Rocky Road","""

METHOD

1. Toast all nuts except the walnuts.
2. Melt chocolate in pan over a medium heat.
3. Add marshmallows and butter, stirring occasionally.
4. Wait until everything has melted.
5. Add nuts and mix well.
6. Spoon mixture onto a buttered tray.
7. Leave in the fridge overnight.
8. The next morning, cut up the cake into squares.

Turn to Page 696 for the ingredients.

Note: You can also add maple syrup!
""")

class RecipeIPage(Page):
    def __init__(self):
        super(RecipeIPage, self).__init__("690")
        self.title = "Recipes Index"

    def generate_content(self):
        self.add_title("Recipes")
        for r in [r1,r2,r3,r4,r5,r6,r7]:
            self.add_text(r.number,bg="BLUE")
            self.add_text(" "+r.title)
            self.add_newline()

rip = RecipeIPage()
