class Utils:

    @staticmethod
    def return_distance_from_string(lib_distance):
        """


                Retrieves the list of distances, converts them to float.

                :return: List with numbers only (distances values).
                """
        distances_list = []
        old_list = [dis.text for dis in lib_distance]
        for distance_str in old_list:
            split_result = distance_str.split()
            distance_number = float(split_result[0])
            distances_list.append(distance_number)
        return distances_list
