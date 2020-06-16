from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import VPC
with Diagram("Web Service", show=False):
    vpc=VPC("VPC")
    vpc >> ELB("lb") >> EC2("web") >> RDS("userdb")
