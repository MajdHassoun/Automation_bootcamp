class Utils:

    @staticmethod
    def wait_for_element(action, expected, time, retries):
        result = action
        while result != expected and retries > 0:
            result = action
            time.sleep(time)
            retries -= retries
