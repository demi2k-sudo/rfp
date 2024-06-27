from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv('OPENAI_API_KEY')


def get_openai_api_key():
    return key


template = """    
| Sl. No | Particulars                           | Description                                                                                                                                                                                                                                 | Page No. |
|--------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 1.     | Bid Name & Address                    |                                                                                                                                                                                                                                             |          |
| 2.     | Name of Client                        |                                                                                                                                                                                                                                             |          |
| 3.     | Date of Tender                        |                                                                                                                                                                                                                                             |          |
| 4.     | Tender No                             |                                                                                                                                                                                                                                             |          |
| 5.     | Due Date                              |                                                                                                                                                                                                                                             |          |
| 6.     | Bid Opening                           |                                                                                                                                                                                                                                             |          |
| 7.     | Place of submission of bid documents  |                                                                                                                                                                                                                                             |          |
| 8.     | Last Date for Clarifications          |                                                                                                                                                                                                                                             |          |
| 9.     | Address for requesting clarifications |                                                                                                                                                                                                                                             |          |
| 10.    | Pre-Bid Meeting                       |                                                                                                                                                                                                                                             |          |
| 11.    | Address of Pre-Bid                    |                                                                                                                                                                                                                                             |          |
| 12.    | Selection Method                      |                                                                                                                                                                                                                                             |          |
| 13.    | Validity of Proposal                  |                                                                                                                                                                                                                                             |          |
| 14.    | Deal Value                            |                                                                                                                                                                                                                                             |          |
| 15.    | EMD                                   |                                                                                                                                                                                                                                             |          |
| 16.    | Tender Doc. Fee                       |                                                                                                                                                                                                                                             |          |
| 17.    | PBG                                   |                                                                                                                                                                                                                                             |          |
| 18.    | Bid System                            |                                                                                                                                                                                                                                             |          |
| 19.    | Scope of work                         |                                                                                                                                                                                                                                             |          |
| 20.    | Deliverables                          |                                                                                                                                                                                                                                             |          |
| 21.    | Competition                           |                                                                                                                                                                                                                                             |          |
| 22.    | Project Location                      |                                                                                                                                                                                                                                             |          |
| 23.    | Eligibility Criteria                  |                                                                                                                                                                                                                                             |          |
| 24.    | Evaluation Criteria                   |                                                                                                                                                                                                                                             |          |
| 25.    | Time schedule                         |                                                                                                                                                                                                                                             |          |
| 26.    | Training                              |                                                                                                                                                                                                                                             |          |
| 27.    | Warranty                              |                                                                                                                                                                                                                                             |          |
| 28.    | AMC                                   |                                                                                                                                                                                                                                             |          |
| 29.    | Bid Currency                          |                                                                                                                                                                                                                                             |          |
| 30.    | Payment Terms                         |                                                                                                                                                                                                                                             |          |
| 31.    | Liquidity Damages/Penalty             |                                                                                                                                                                                                                                             |          |
| 32.    | Demo/PoC/Tech Presentation            |                                                                                                                                                                                                                                             |          |
| 33.    | Documents to Enclose/Information to share |                                                                                                                                                                                                                                             |          |
| 34.    | Others                                |                                                                                                                                                                                                                                             |          |

    """
