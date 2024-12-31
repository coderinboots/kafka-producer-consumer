# kafka-producer-consumer
This project contains the python programs for simple kafka producer and consumer

# The project has a single producer and 3 consumers
The producer produces the message

1st and second consumers are part of the same consumer group. Both will work together. 
3rd consumer is part of a different consumer group. So the messages will be processed independently and will not work together with the consumers in the first consumer group. 
