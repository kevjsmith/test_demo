# Sample Mermaid Diagram As Code

## Application Dependency Diagram

### This is a test

``` mermaid
    flowchart LR
        subgraph "USA"
            subgraph "Subgraph #1 Heading"
            A[name]
            B[name]
            C[name]
            end
        end
        subgraph "Subgraph #2 Heading"
            D
            E
            F
        end
        subgraph "Subgraph #3 Heading"
            G
            H
            I
        end      

        A <--tcp/443--> D
        B --tcp/443--> E
        C --tcp/443--> F
        D --tcp/443--> G
        E --tcp/443--> G
        I --tcp/443--> MKT--> FW{Internal Firewall}
```

``` mermaid
graph LR
    MKT[Marketing App Server] -- TCP 443 --> FW{Internal Firewall}
    FW -- BLOCK --> HR[HR Server]
    style FW fill:#fff,stroke:#000
```

