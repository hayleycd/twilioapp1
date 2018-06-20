import authentication
import random

POTENTIAL_GOLDEN_RETRIEVER_NAMES = ["Cupcake Von Sunshine",
                                    "Pascal",
                                    "Sunset",
                                    "Rei",
                                    "Daffodil",
                                    "Strawberry",
                                    "Holmes",
                                    "Watson",
                                    "Jean Valjean"]

dog_message = "Hi Babe! I think we should get a Golden Retriever and name it {}. Love from Hayley"

message = authentication.client.messages.create(
                                            body=dog_message
                                            .format(POTENTIAL_GOLDEN_RETRIEVER_NAMES[random.randrange(10)]),
                                            from_=authentication.my_twilio_number,
                                            to=authentication.my_partners_mobile_number
                                        )

print(message)
print(message.body)