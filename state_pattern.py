from abc import ABC, abstractmethod

# Interface State
class State(ABC):
    @abstractmethod
    def move(self) -> str:
        pass
    
    @abstractmethod
    def attack(self) -> str:
        pass
    
    @abstractmethod
    def receive_damage(self) -> str:
        pass

# Estados Concretos
class NormalState(State):
    def move(self) -> str:
        return "Moviéndose a velocidad normal"
    
    def attack(self) -> str:
        return "Realizando ataque normal - 10 de daño"
    
    def receive_damage(self) -> str:
        return "Recibiendo daño normal - 10 de daño recibido"

class PoweredState(State):
    def move(self) -> str:
        return "Moviéndose a velocidad aumentada (+50%)"
    
    def attack(self) -> str:
        return "Realizando ataque potenciado - 20 de daño"
    
    def receive_damage(self) -> str:
        return "Recibiendo daño reducido - 5 de daño recibido"

class InjuredState(State):
    def move(self) -> str:
        return "Moviéndose lentamente (-50% velocidad)"
    
    def attack(self) -> str:
        return "Realizando ataque débil - 5 de daño"
    
    def receive_damage(self) -> str:
        return "Recibiendo daño crítico - 20 de daño recibido"

class ImmuneState(State):
    def move(self) -> str:
        return "Moviéndose a velocidad normal"
    
    def attack(self) -> str:
        return "Realizando ataque normal - 10 de daño"
    
    def receive_damage(self) -> str:
        return "Inmune al daño - 0 de daño recibido"

# Clase Contexto
class Character:
    def __init__(self):
        self._state = NormalState()
    
    def change_state(self, state: State):
        self._state = state
        return f"Estado cambiado a {state.__class__.__name__}"
    
    def move(self) -> str:
        return self._state.move()
    
    def attack(self) -> str:
        return self._state.attack()
    
    def receive_damage(self) -> str:
        return self._state.receive_damage()

# Ejemplo de uso
def main():
    character = Character()
    
    # Estado Normal
    print("Estado Normal:")
    print(character.move())
    print(character.attack())
    print(character.receive_damage())
    
    # Cambio a Estado Potenciado
    print("\nCambiando a Estado Potenciado:")
    print(character.change_state(PoweredState()))
    print(character.move())
    print(character.attack())
    print(character.receive_damage())
    
    # Cambio a Estado Herido
    print("\nCambiando a Estado Herido:")
    print(character.change_state(InjuredState()))
    print(character.move())
    print(character.attack())
    print(character.receive_damage())
    
    # Cambio a Estado Inmune
    print("\nCambiando a Estado Inmune:")
    print(character.change_state(ImmuneState()))
    print(character.move())
    print(character.attack())
    print(character.receive_damage())

if __name__ == "__main__":
    main()