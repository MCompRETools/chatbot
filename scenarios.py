SCENARIO = {
    "title": "Sustainable Cloud Migration",
    "context": """
You are the Digital Strategy Lead at a retail company planning to migrate
to a cloud-based analytics platform while meeting sustainability targets.
""",
    "decisions": [
        {
            "id": "cloud_provider",
            "question": "Which cloud provider do you select?",
            "options": {
                "Low-cost provider with fossil energy": {"env": -2, "econ": +2, "soc": 0, "gov": -1},
                "Renewable-powered provider": {"env": +2, "econ": -1, "soc": +1, "gov": +1},
                "Hybrid approach": {"env": +1, "econ": 0, "soc": 0, "gov": 0}
            }
        },
        {
            "id": "data_strategy",
            "question": "How will customer data be managed?",
            "options": {
                "Collect all available data": {"env": -1, "econ": +1, "soc": -2, "gov": -1},
                "Data minimization approach": {"env": +1, "econ": 0, "soc": +2, "gov": +1}
            }
        }
    ]
}
