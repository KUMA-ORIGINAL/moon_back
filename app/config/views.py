from rest_framework.views import APIView
from rest_framework.response import Response

class AboutView(APIView):
    def get(self, request):
        data = {
            "title": "ABOUT MOON",
            "description": "Moon’s handcrafted ceramic products have been around since 1990. We continue our journey.",
            "imageUrl": "",
            "timeline": [
                {
                    "year": "1910",
                    "description": "Lorem ipsum dolor sit amet consectetur adipiscing elit morbi et pharetra et ultrices neque ornare.",
                    "imageUrl": "http://localhost:5173/src/assets/images/About%20Moon/Image1.png"
                },
                {
                    "year": "1990",
                    "description": "Maecenas sem eros, rutrum vitae massa eget, vulputate ornare nulla. Aenean vitae risus eget, vulputate sapien nec.",
                    "imageUrl": "http://localhost:5173/src/assets/images/About%20Moon/Image2.png"
                },
                {
                    "year": "2010",
                    "description": "Fusce vitae lacus vitae sapien vulputate bibendum nec ac gravida neque. Morbi ac dignissim ex rutrum vitae risus.",
                    "imageUrl": "http://localhost:5173/src/assets/images/About%20Moon/Image3.png"
                }
            ],
            "works": {
                "title": "HOW WE WORKS",
                "description": "",
                "imageUrl": "http://localhost:5173/src/assets/images/About%20Moon/Image3.png",
                "steps": [
                    {
                        "title": "Product design",
                        "description": "Lorem ipsum dolor sit amet consectetur adipiscing elit morbi et pharetra et ultrices neque ornare."
                    },
                    {
                        "title": "Crafted",
                        "description": "Nullam vehicula, mi eget tincidunt feugiat, velit nibh placerat odio, at gravida risus neque id."
                    },
                    {
                        "title": "Sell product",
                        "description": "Aenean vitae risus eget, vulputate sapien nec, vulputate justo."
                    }
                ]
            },
            "team": {
                "title": "MEET OUR TEAM",
                "description": "",
                "imageUrl": "",
                "members": [
                    {
                        "name": "BYRONE RUTTERFORD",
                        "position": "CEO & Founder",
                        "imageUrl": "http://localhost:5173/src/assets/images/Our%20Team/Image1.png"
                    },
                    {
                        "name": "CHARLIE WU",
                        "position": "Creative Director",
                        "imageUrl": "http://localhost:5173/src/assets/images/Our%20Team/Image2.png"
                    },
                    {
                        "name": "COREEN HOSSAIN",
                        "position": "Artist",
                        "imageUrl": "http://localhost:5173/src/assets/images/Our%20Team/Image3.png"
                    },
                    {
                        "name": "SARAH BONNE",
                        "position": "Marketing",
                        "imageUrl": "http://localhost:5173/src/assets/images/Our%20Team/Image4.png"
                    }
                ]
            }
        }
        return Response(data)


class HomeView(APIView):
    def get(self, request):
        data = {
            "imageUrl": "",
            "description": "",
            "pepls": [
                {
                    "id": 1,
                    "title": "TableWare",
                    "imageUrl": "http://localhost:5173/src/assets/images/Demo/Image1.png"
                },
                {
                    "id": 2,
                    "title": "TableWare",
                    "imageUrl": "http://localhost:5173/src/assets/images/Demo/Image2.png"
                },
                {
                    "id": 3,
                    "title": "TableWare",
                    "imageUrl": "http://localhost:5173/src/assets/images/Demo/Image3.png"
                },
                {
                    "id": 4,
                    "title": "TableWare",
                    "imageUrl": "http://localhost:5173/src/assets/images/Demo/Image4.png"
                }
            ],
            "promo": {
                "title": "Up to 40% off our Christmas Collection",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Learn more about our seasonal discounts.",
                "imageUrl": "http://localhost:5173/src/assets/images/Pottery/img2.png",
                "buttonText": "SHOP NOW"
            },
            "history": [
                {
                    "title": "MADE IN VIET NAM SINCE 1450",
                    "description": "Lorem ipsum dolor sit amet consectetur adipiscing eli mattis sit phasellus mollis sit aliquam sit nullam neque ultrices.",
                    "imageUrl": "src/assets/images/Pottery/img1.png",
                    "buttonText": "LEARN MORE"
                },
                {
                    "title": "OUR HISTORY",
                    "description": "Lorem ipsum dolor sit amet consectetur adipiscing eli mattis sit phasellus mollis sit aliquam sit",
                    "imageUrl": "src/assets/images/Pottery/img2.png",
                    "buttonText": "LEARN MORE"
                }
            ],
            "blog": {
                "title": "THE SECRETS TO A KITCHEN ROOM",
                "description": "Lorem ipsum dolor sit amet consectetur adipiscing elit mattis sit phasellus mollis sit aliquam sit nullam neque ultrices..",
                "imageUrl": "http://localhost:5173/src/assets/images/OurBlog/img1.png",
                "buttonText": "READ MORE"
            }
        }
        return Response(data)
