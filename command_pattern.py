from abc import ABC, abstractmethod
from typing import List, Optional

# Receptor
class MusicPlayer:
    def __init__(self):
        self.is_playing = False
        self.volume = 50
        self.current_track: Optional[str] = None
    
    def play(self):
        self.is_playing = True
        return f"Reproduciendo música. Volumen: {self.volume}"
    
    def pause(self):
        self.is_playing = False
        return "Música pausada"
    
    def set_volume(self, volume: int):
        old_volume = self.volume
        self.volume = max(0, min(100, volume))  # Asegurar que esté entre 0 y 100
        return f"Volumen cambiado de {old_volume} a {self.volume}"

# Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass
    
    @abstractmethod
    def undo(self) -> str:
        pass

# Comandos Concretos
class PlayCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player
    
    def execute(self) -> str:
        return self.player.play()
    
    def undo(self) -> str:
        return self.player.pause()

class PauseCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player
    
    def execute(self) -> str:
        return self.player.pause()
    
    def undo(self) -> str:
        return self.player.play()

class VolumeCommand(Command):
    def __init__(self, player: MusicPlayer, volume: int):
        self.player = player
        self.prev_volume = player.volume
        self.new_volume = volume
    
    def execute(self) -> str:
        return self.player.set_volume(self.new_volume)
    
    def undo(self) -> str:
        return self.player.set_volume(self.prev_volume)

# Invocador
class MusicController:
    def __init__(self):
        self._history: List[Command] = []
    
    def execute_command(self, command: Command) -> str:
        self._history.append(command)
        return command.execute()
    
    def undo_last_command(self) -> str:
        if self._history:
            command = self._history.pop()
            return command.undo()
        return "No hay comandos para deshacer"

# Ejemplo de uso
def main():
    # Crear el reproductor y el controlador
    player = MusicPlayer()
    controller = MusicController()
    
    # Crear comandos
    play_command = PlayCommand(player)
    pause_command = PauseCommand(player)
    volume_up_command = VolumeCommand(player, 75)
    volume_down_command = VolumeCommand(player, 25)
    
    # Ejecutar comandos
    print("Ejecutando comandos:")
    print(controller.execute_command(play_command))
    print(controller.execute_command(volume_up_command))
    print(controller.execute_command(pause_command))
    print(controller.execute_command(volume_down_command))
    
    # Deshacer comandos
    print("\nDeshaciendo comandos:")
    print(controller.undo_last_command())  # Deshace volume_down
    print(controller.undo_last_command())  # Deshace pause
    print(controller.undo_last_command())  # Deshace volume_up
    print(controller.undo_last_command())  # Deshace play

if __name__ == "__main__":
    main()