import json
class PositionDatabase:
    def __init__(self, source_type="mock"):
        self.source_type = source_type

    def load_positions(self):
        if self.source_type == "mock":
            raw_json_data = """ [
  {
    "id": 1,
    "title": "PhD in Efficient Machine Learning",
    "description": "Developing sparse neural networks and quantization techniques for edge devices. Requires strong C++ and CUDA skills.",
    "requirements": {
      "minimum_gre_score": 325,
      "minimum_gpa": 3.8,
      "deadline": "2025-12-15"
    },
    "university": {
      "name": "Massachusetts Institute of Technology (MIT)",
      "location": "Cambridge, USA",
      "ranking": 1
    },
    "professor": {
      "name": "Dr. Song Han",
      "email": "songhan@mit.edu",
      "research_interests": ["Efficient AI", "Hardware-Aware NAS"]
    },
    "apply_cost": {
      "currency": "USD",
      "amount": 75
    }
  },
  {
    "id": 2,
    "title": "PhD in Neuromorphic Computing",
    "description": "Research on spiking neural networks and brain-inspired hardware architectures.",
    "requirements": {
      "minimum_gre_score": 310,
      "minimum_gpa": 3.5,
      "deadline": "2025-01-31"
    },
    "university": {
      "name": "Technical University of Munich (TUM)",
      "location": "Munich, Germany",
      "ranking": 28
    },
    "professor": {
      "name": "Dr. Alois Knoll",
      "email": "knoll@in.tum.de",
      "research_interests": ["Robotics", "Neuromorphic Systems"]
    },
    "apply_cost": {
      "currency": "EUR",
      "amount": 0
    }
  },
  {
    "id": 3,
    "title": "PhD in Reinforcement Learning",
    "description": "Focus on offline RL and safety in autonomous driving agents.",
    "requirements": {
      "minimum_gre_score": 320,
      "minimum_gpa": 3.7,
      "deadline": "2025-01-10"
    },
    "university": {
      "name": "University of Toronto",
      "location": "Toronto, Canada",
      "ranking": 21
    },
    "professor": {
      "name": "Dr. Sheila McIlraith",
      "email": "sheila@cs.toronto.edu",
      "research_interests": ["KR", "Reinforcement Learning"]
    },
    "apply_cost": {
      "currency": "CAD",
      "amount": 125
    }
  },
  {
    "id": 4,
    "title": "PhD in Computer Vision",
    "description": "3D scene reconstruction and nerf fields for AR/VR applications.",
    "requirements": {
      "minimum_gre_score": 315,
      "minimum_gpa": 3.3,
      "deadline": "2025-03-01"
    },
    "university": {
      "name": "ETH Zurich",
      "location": "Zurich, Switzerland",
      "ranking": 7
    },
    "professor": {
      "name": "Dr. Marc Pollefeys",
      "email": "marc.pollefeys@inf.ethz.ch",
      "research_interests": ["Computer Vision", "3D Reconstruction"]
    },
    "apply_cost": {
      "currency": "CHF",
      "amount": 0
    }
  },
  {
    "id": 5,
    "title": "PhD in NLP & Large Language Models",
    "description": "Researching reasoning capabilities and hallucination reduction in LLMs.",
    "requirements": {
      "minimum_gre_score": 328,
      "minimum_gpa": 3.9,
      "deadline": "2024-12-01"
    },
    "university": {
      "name": "Stanford University",
      "location": "California, USA",
      "ranking": 2
    },
    "professor": {
      "name": "Dr. Christopher Manning",
      "email": "manning@stanford.edu",
      "research_interests": ["NLP", "Deep Learning"]
    },
    "apply_cost": {
      "currency": "USD",
      "amount": 125
    }
  },
  {
    "id": 6,
    "title": "PhD in AI for Healthcare",
    "description": "Using federated learning for privacy-preserving medical data analysis.",
    "requirements": {
      "minimum_gre_score": 300,
      "minimum_gpa": 3.2,
      "deadline": "2025-04-15"
    },
    "university": {
      "name": "University of Alberta",
      "location": "Edmonton, Canada",
      "ranking": 110
    },
    "professor": {
      "name": "Dr. Osmar Zaiane",
      "email": "zaiane@ualberta.ca",
      "research_interests": ["Data Mining", "Health Informatics"]
    },
    "apply_cost": {
      "currency": "CAD",
      "amount": 100
    }
  },
  {
    "id": 7,
    "title": "PhD in Robotics Systems",
    "description": "Design of soft robotics and control systems for human-robot interaction.",
    "requirements": {
      "minimum_gre_score": 310,
      "minimum_gpa": 3.4,
      "deadline": "2025-02-28"
    },
    "university": {
      "name": "Delft University of Technology",
      "location": "Delft, Netherlands",
      "ranking": 48
    },
    "professor": {
      "name": "Dr. Jens Kober",
      "email": "j.kober@tudelft.nl",
      "research_interests": ["Robotics", "Machine Learning"]
    },
    "apply_cost": {
      "currency": "EUR",
      "amount": 0
    }
  },
  {
    "id": 8,
    "title": "PhD in Distributed Systems",
    "description": "Scalable consensus algorithms for blockchain and distributed ledgers.",
    "requirements": {
      "minimum_gre_score": 318,
      "minimum_gpa": 3.6,
      "deadline": "2025-01-20"
    },
    "university": {
      "name": "EPFL",
      "location": "Lausanne, Switzerland",
      "ranking": 16
    },
    "professor": {
      "name": "Dr. Rachid Guerraoui",
      "email": "rachid.guerraoui@epfl.ch",
      "research_interests": ["Distributed Computing", "Algorithms"]
    },
    "apply_cost": {
      "currency": "CHF",
      "amount": 50
    }
  },
  {
    "id": 9,
    "title": "PhD in AI Safety and Alignment",
    "description": "Ensuring AI systems align with human values and robust decision making.",
    "requirements": {
      "minimum_gre_score": 325,
      "minimum_gpa": 3.8,
      "deadline": "2024-12-15"
    },
    "university": {
      "name": "University of Oxford",
      "location": "Oxford, UK",
      "ranking": 4
    },
    "professor": {
      "name": "Dr. Yarin Gal",
      "email": "yarin.gal@cs.ox.ac.uk",
      "research_interests": ["Bayesian Deep Learning", "AI Safety"]
    },
    "apply_cost": {
      "currency": "GBP",
      "amount": 75
    }
  },
  {
    "id": 10,
    "title": "PhD in Graph Neural Networks",
    "description": "Applying GNNs to molecular discovery and drug design.",
    "requirements": {
      "minimum_gre_score": 305,
      "minimum_gpa": 3.1,
      "deadline": "2025-05-30"
    },
    "university": {
      "name": "Mila - Quebec AI Institute",
      "location": "Montreal, Canada",
      "ranking": 30
    },
    "professor": {
      "name": "Dr. Jian Tang",
      "email": "jian.tang@hec.ca",
      "research_interests": ["Graph Learning", "Drug Discovery"]
    },
    "apply_cost": {
      "currency": "CAD",
      "amount": 115
    }
  },
  {
    "id": 11,
    "title": "PhD in Cloud Computing",
    "description": "Serverless computing optimization and resource scheduling in cloud environments.",
    "requirements": {
      "minimum_gre_score": 312,
      "minimum_gpa": 3.3,
      "deadline": "2025-02-15"
    },
    "university": {
      "name": "University of Melbourne",
      "location": "Melbourne, Australia",
      "ranking": 34
    },
    "professor": {
      "name": "Dr. Rajkumar Buyya",
      "email": "rbuyya@unimelb.edu.au",
      "research_interests": ["Cloud Computing", "IoT"]
    },
    "apply_cost": {
      "currency": "AUD",
      "amount": 100
    }
  },
  {
    "id": 12,
    "title": "PhD in Explainable AI (XAI)",
    "description": "Developing methods to interpret deep learning models for financial applications.",
    "requirements": {
      "minimum_gre_score": 308,
      "minimum_gpa": 3.5,
      "deadline": "2025-03-20"
    },
    "university": {
      "name": "National University of Singapore (NUS)",
      "location": "Singapore",
      "ranking": 8
    },
    "professor": {
      "name": "Dr. Reza Shokri",
      "email": "reza@comp.nus.edu.sg",
      "research_interests": ["Data Privacy", "Trustworthy ML"]
    },
    "apply_cost": {
      "currency": "SGD",
      "amount": 50
    }
  },
  {
    "id": 13,
    "title": "PhD in Computer Architecture",
    "description": "Designing next-generation accelerators for sparse tensor operations.",
    "requirements": {
      "minimum_gre_score": 320,
      "minimum_gpa": 3.7,
      "deadline": "2024-12-01"
    },
    "university": {
      "name": "Georgia Tech",
      "location": "Atlanta, USA",
      "ranking": 38
    },
    "professor": {
      "name": "Dr. Tushar Krishna",
      "email": "tushar@ece.gatech.edu",
      "research_interests": ["NoC", "AI Accelerators"]
    },
    "apply_cost": {
      "currency": "USD",
      "amount": 85
    }
  },
  {
    "id": 14,
    "title": "PhD in Cybersecurity & Crypto",
    "description": "Post-quantum cryptography and secure multi-party computation.",
    "requirements": {
      "minimum_gre_score": 316,
      "minimum_gpa": 3.4,
      "deadline": "2025-01-15"
    },
    "university": {
      "name": "Ruhr University Bochum",
      "location": "Bochum, Germany",
      "ranking": 200
    },
    "professor": {
      "name": "Dr. Eike Kiltz",
      "email": "eike.kiltz@rub.de",
      "research_interests": ["Cryptography", "Security"]
    },
    "apply_cost": {
      "currency": "EUR",
      "amount": 0
    }
  },
  {
    "id": 15,
    "title": "PhD in Human-Computer Interaction",
    "description": "Augmented reality interfaces for remote collaboration.",
    "requirements": {
      "minimum_gre_score": 305,
      "minimum_gpa": 3.2,
      "deadline": "2025-02-10"
    },
    "university": {
      "name": "University of British Columbia",
      "location": "Vancouver, Canada",
      "ranking": 34
    },
    "professor": {
      "name": "Dr. Karon MacLean",
      "email": "macLean@cs.ubc.ca",
      "research_interests": ["HCI", "Haptics"]
    },
    "apply_cost": {
      "currency": "CAD",
      "amount": 110
    }
  },
  {
    "id": 16,
    "title": "PhD in Databases",
    "description": "Optimizing database engines for non-volatile memory (NVM).",
    "requirements": {
      "minimum_gre_score": 315,
      "minimum_gpa": 3.5,
      "deadline": "2025-01-05"
    },
    "university": {
      "name": "Carnegie Mellon University",
      "location": "Pittsburgh, USA",
      "ranking": 25
    },
    "professor": {
      "name": "Dr. Andy Pavlo",
      "email": "pavlo@cs.cmu.edu",
      "research_interests": ["Database Systems", "Self-Driving DBMS"]
    },
    "apply_cost": {
      "currency": "USD",
      "amount": 100
    }
  },
  {
    "id": 17,
    "title": "PhD in Software Engineering",
    "description": "Automated bug fixing and code generation using LLMs.",
    "requirements": {
      "minimum_gre_score": 300,
      "minimum_gpa": 3.1,
      "deadline": "2025-03-30"
    },
    "university": {
      "name": "KTH Royal Institute of Technology",
      "location": "Stockholm, Sweden",
      "ranking": 89
    },
    "professor": {
      "name": "Dr. Martin Monperrus",
      "email": "monperrus@kth.se",
      "research_interests": ["Software Repair", "DevOps"]
    },
    "apply_cost": {
      "currency": "SEK",
      "amount": 900
    }
  },
  {
    "id": 18,
    "title": "PhD in Quantum Computing",
    "description": "Quantum error correction and quantum algorithms for optimization.",
    "requirements": {
      "minimum_gre_score": 320,
      "minimum_gpa": 3.6,
      "deadline": "2025-02-01"
    },
    "university": {
      "name": "University of Waterloo",
      "location": "Waterloo, Canada",
      "ranking": 112
    },
    "professor": {
      "name": "Dr. Raymond Laflamme",
      "email": "laflamme@iqc.ca",
      "research_interests": ["Quantum Information", "Physics"]
    },
    "apply_cost": {
      "currency": "CAD",
      "amount": 125
    }
  },
  {
    "id": 19,
    "title": "PhD in Mobile Computing",
    "description": "Battery-efficient sensing for wearable health devices.",
    "requirements": {
      "minimum_gre_score": 308,
      "minimum_gpa": 3.3,
      "deadline": "2025-04-10"
    },
    "university": {
      "name": "Dartmouth College",
      "location": "Hanover, USA",
      "ranking": 200
    },
    "professor": {
      "name": "Dr. Andrew Campbell",
      "email": "campbell@cs.dartmouth.edu",
      "research_interests": ["Mobile Sensing", "Health Tech"]
    },
    "apply_cost": {
      "currency": "USD",
      "amount": 80
    }
  },
  {
    "id": 20,
    "title": "PhD in Computational Neuroscience",
    "description": "Modeling visual cortex using deep neural networks.",
    "requirements": {
      "minimum_gre_score": 318,
      "minimum_gpa": 3.7,
      "deadline": "2025-01-25"
    },
    "university": {
      "name": "Tubingen University",
      "location": "Tubingen, Germany",
      "ranking": 78
    },
    "professor": {
      "name": "Dr. Matthias Bethge",
      "email": "matthias.bethge@uni-tuebingen.de",
      "research_interests": ["Computational Neuroscience", "Machine Learning"]
    },
    "apply_cost": {
      "currency": "EUR",
      "amount": 0
    }
  }
]"""
            return json.loads(raw_json_data)
        
        elif self.source_type == "production":
            # return database.connect("postgres://...").query(...)
            pass


# ==============================================================================
# 2. TOOL: Market Data Fetcher
# ==============================================================================
def fetch_positions_tool() -> str:
    """
    Fetches the list of open academic positions from the database.
    Returns: A JSON string of available positions.
    """
    db = PositionDatabase(source_type="mock")
    positions = db.load_positions()
    print(f"✅ Database Loaded: {len(positions)} positions.")
    return json.dumps(positions)