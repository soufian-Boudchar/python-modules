import time
import functools

def spell_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int, max_power: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(power, *args, **kwargs):
            if power < min_power or power > max_power:
                raise ValueError("Insufficient power for this spell")
            return func(power, *args, **kwargs)
        return wrapper
    return decorator

def retry_spell(max_retries: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_retries:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_retries})")
                    else:
                        print(f"Spell casting failed after {max_retries} attempts")
                        raise e
        return wrapper
    return decorator

@spell_timer
def fireball():
    time.sleep(0.101)
    return "Result: Fireball cast!"

@retry_spell(max_retries=3)
def failing_spell():
    raise Exception("Waaaaaaagh spelled !")

@power_validator(10, 50)
def cast_lightning(power):
    return f"Successfully cast Lightning with {power} power"

if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())
    print()
    print("Testing retrying spell...")
    try:
        failing_spell()
    except Exception as e:
        print(e)
        
    print("Testing MageGuild...")
    print()
    print(True)
    print(False)
    try:
        print(cast_lightning(15))
        print(cast_lightning(5))
    except Exception as e:
        print(e)