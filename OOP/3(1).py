import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class SpaceObject:
    """Общий класс для космического тела: планеты или звезды."""

    def __init__(self, m, x, y, Vx, Vy, R, color, object_type):
        self.type = object_type
        self.m = m  # Масса
        self.x = x  # Координата x
        self.y = y  # Координата y
        self.Vx = Vx  # Скорость по x
        self.Vy = Vy  # Скорость по y
        self.Fx = 0  # Сила по x
        self.Fy = 0  # Сила по y
        self.R = R  # Радиус объекта
        self.color = color  # Цвет объекта
        self.image = None  # Изображение 

    def reset_force(self):
        self.Fx = 0
        self.Fy = 0


class Star(SpaceObject):
    def __init__(self, m, x, y, Vx, Vy, R=10, color="yellow"):
        super().__init__(m, x, y, Vx, Vy, R, color, "star")


class Planet(SpaceObject):
    def __init__(self, m, x, y, Vx, Vy, R=5, color="green"):
        super().__init__(m, x, y, Vx, Vy, R, color, "planet")


def calculate_force(body, space_objects):
    """Вычисляет гравитационную силу, действующую на тело."""
    body.reset_force()
    for obj in space_objects:
        if body == obj:  
            continue

        dx = obj.x - body.x
        dy = obj.y - body.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance == 0:  
            continue

        force = gravitational_constant * body.m * obj.m / distance ** 2  # Закон всемирного тяготения
        Fx = force * (dx / distance)  # Проекция силы на x
        Fy = force * (dy / distance)  # Проекция силы на y

        body.Fx += Fx
        body.Fy += Fy


def move_space_object(body, dt):
    ax = body.Fx / body.m  # Ускорение по x
    ay = body.Fy / body.m  # Ускорение по y

    # Обновляем скорости с учётом ускорения
    body.Vx += ax * dt
    body.Vy += ay * dt

    # Обновляем координаты с учётом скорости
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    for body in space_objects:
        calculate_force(body, space_objects)

    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    star = Star(m=1.989e30, x=0, y=0, Vx=0, Vy=0)  # Масса Солнца, координаты 0,0
    planet = Planet(m=5.972e24, x=1.496e11, y=0, Vx=0, Vy=29780)  # Масса Земли, орбита 1 а.е., скорость 29.78 км/с

    space_objects = [star, planet]

    # Шаг по времени (одни сутки)
    dt = 86400

    # Моделируем движение на протяжении 10 дней
    for day in range(10):
        recalculate_space_objects_positions(space_objects, dt)
        print(f"Day {day + 1}:")
        print(f"  Planet position: x = {planet.x:.2e}, y = {planet.y:.2e}")
        print(f"  Planet velocity: Vx = {planet.Vx:.2e}, Vy = {planet.Vy:.2e}")
