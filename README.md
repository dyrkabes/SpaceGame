--- Development is on hold bc I am deep in swift atm ---

# SpaceGame
Space game inspired by SpaceRangers, FTL and some others

At the moment I am refactoring and documenting the code so I can move towards

Video example https://www.youtube.com/watch?v=uAq_awz5tZg

Brief description:

1. Player manipulates one ship, he can move around, shoot, collect comets' chunks
2. AI driven ships for now move in random directions aiming player's ship only
3. Comets are randomly generated, for now they're moving all the ways around. Star effects them with gravity
4. Player ship consists of components like engine, weapon etc.
5. Components consist of modules which determine component's stats like rotation speed or bullet damage. 
6. Modules can effect in both positive and negative ways. For instance, a module could speed up bullet and make it deal a lot of damage but slow down the reload speed
7. In inventory it is possible to look to ship's components and its modules and their characteristics but there's still no way to swap components or modules in game


What's next:

1. Possibility to swap components and modules from inventory
2. More complex module behaviour
3. Different types of bullets (rocket, fragmentable)
4. Different types of aiming - not only directly on the ship but for instance just in a particular point in space
5. Planets: landing, trading
6. Quests
7. Different types of enviromental AI driven ships: pirates, miners, traders
Seems enough for now :D
