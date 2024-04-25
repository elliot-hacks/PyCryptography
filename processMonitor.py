import pygame
import sys,os
import psutil
import datetime


pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FONT_SIZE = 20
font = pygame.font.SysFont(None, FONT_SIZE)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("System Monitor")

clock = pygame.time.Clock()


def draw_bar(x, y, width, height, color, value):
    fill_width = width * (value / 100)
    pygame.draw.rect(screen, color, (x, y, fill_width, height))


def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((30, 30, 30))


        memory = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent()
        processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent'])
        top_processes = sorted(processes, key=lambda p: p.info['cpu_percent'], reverse=True)[:10]
        partitions = psutil.disk_partitions()
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        battery = psutil.sensors_battery()


        draw_text(f"Memory Usage: {memory.percent}%", 20, 20, GREEN)
        draw_bar(180, 20, 200, 20, GREEN, memory.percent)


        draw_text(f"CPU Usage: {cpu_percent}%", 20, 50, RED)
        draw_bar(180, 50, 200, 20, RED, cpu_percent)

 
        draw_text("Disk Partitions:", 20, 80, BLUE)
        y_offset = 110
        for partition in psutil.disk_partitions():
            partition_usage = psutil.disk_usage(partition.mountpoint)
            draw_text(f"{partition.device} - {partition.mountpoint}", 40, y_offset)
            draw_text(f"Total: {partition_usage.total / (1024 ** 3):.2f} GB", 60, y_offset + 25)
            draw_text(f"Used: {partition_usage.used / (1024 ** 3):.2f} GB", 60, y_offset + 50)
            draw_text(f"Free: {partition_usage.free / (1024 ** 3):.2f} GB", 60, y_offset + 75)
            draw_text(f"Usage: {partition_usage.percent}%", 60, y_offset + 100, GREEN)
            y_offset += 150


        draw_text(f"Boot Time: {boot_time}", 20, y_offset, GREEN)
        y_offset += 25


        if battery:
            draw_text(f"Battery: {battery.percent}%", 20, y_offset, RED)

            if battery.power_plugged:
                draw_text("Status: Charging", 20, y_offset + 25, GREEN)
            else:
                remaining_time = battery.secsleft
                if remaining_time > 0:
                    hours, remainder = divmod(remaining_time, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    draw_text(f"Remaining Time: {hours}h {minutes}m {seconds}s", 20, y_offset + 25, GREEN)
                else:
                    draw_text("Status: Fully Charged", 20, y_offset + 25, GREEN)

            y_offset += 50


        draw_text("Top 10 Processes:", 20, y_offset, BLUE)
        y_offset += 30
        processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent'])
        top_processes = sorted(processes, key=lambda p: p.info['cpu_percent'], reverse=True)[:10]
        for idx, process in enumerate(top_processes):
            draw_text(f"{idx + 1}. {process.info['name']} - {process.info['cpu_percent']}%", 40, y_offset)
            y_offset += 25


        draw_text("Environment Variables:", 500, 20, BLUE)
        y_offset_env = 50
        for key, value in os.environ.items():
            draw_text(f"{key}: {value}", 520, y_offset_env)
            y_offset_env += 25


        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
