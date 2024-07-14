import time


class Utils:
    @staticmethod
    def wait_for_element(action, expected, wait_time, retries):
        """
        Wait for an action to produce an expected result within a specified time and retry count.

        :param action: The action or function to execute.
        :param expected: The expected result to wait for.
        :param wait_time: The time (in seconds) to wait before retrying.
        :param retries: The number of retries before giving up.
        :return: The result of the action when it matches the expected result or retries are exhausted.
        """
        result = action()
        while result != expected and retries > 0:
            result = action()
            time.sleep(wait_time)
            retries -= 1
        return result

    @staticmethod
    def return_distance_from_string(lib_distance):
        """


                Retrieves the list of distances, converts them to float.

                :return: List with numbers only (distances values).
                """
        distances_list = []
        old_list = [dis.text for dis in lib_distance]
        for distance in old_list:
            split_result = distance.split()
            distance_number = float(split_result[0])
            distances_list.append(distance_number)
        return distances_list
