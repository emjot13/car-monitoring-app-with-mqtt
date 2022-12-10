from mqtt import battery, fuel, engine, brakes_fluid, oil, tires
import threading


def launch():
    sensors = [
        battery.main,
        brakes_fluid.main,
        engine.main,
        fuel.main,
        oil.main,
        tires.main]
    jobs = [threading.Thread(target=sensor, args=(10,)) for sensor in sensors]
    for job in jobs:
        job.start()


if __name__ == '__main__':
    launch()
