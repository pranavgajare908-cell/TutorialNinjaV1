import datetime
from datetime import datetime
import os


class Screenshot:
    @staticmethod
    def capture(driver, test_name):
        folder=os.path.join(os.getcwd(), "screenshots")
        os.makedirs(folder, exist_ok=True)

        filename=f"{test_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        path=os.path.join(folder, filename)
        driver.save_screenshot(path)
        print("Screenshot saved to ", path)
        return path

