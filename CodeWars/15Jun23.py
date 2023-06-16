import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_queue_time(customers, num_tills):
    """
    Calculates the total time it takes for all customers to be served given the number of tills available.

    :param customers: List of integers representing the time it takes for each customer to be served.
    :type customers: list
    :param num_tills: Number of tills available.
    :type num_tills: int
    :return: Total time it takes for all customers to be served.
    :rtype: int
    """

    # Validate input
    if not isinstance(customers, list) or not all(
        isinstance(i, int) for i in customers
    ):
        logger.error("Customers must be a list of integers.")
        raise TypeError("Customers must be a list of integers.")
    if not isinstance(num_tills, int):
        logger.error("Number of tills must be an integer.")
        raise TypeError("Number of tills must be an integer.")

    # Initialize checkout list with zeros
    checkout = [0] * num_tills

    # Serve customers and update checkout list
    for customer in customers:
        checkout[checkout.index(min(checkout))] += customer

    # Calculate total time it takes for all customers to be served
    total_time = max(checkout)

    # Log total time
    logger.info("Total time to serve all customers: %s", total_time)

    return total_time


print(calculate_queue_time([10, 2, 3, 3], 2))
