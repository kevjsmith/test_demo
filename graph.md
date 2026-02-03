# Title

``` mermaid

graph LR
    subgraph Production
        MKT[Marketing App Server]
    end

    subgraph Development
        HR[Human Resources Server]
    end

    %% Lateral Movement Connection
    MKT -- "TCP 443 (Lateral Movement)" --> HR

    %% Styling for clarity
    style MKT fill:#f96,stroke:#333,stroke-width:2px
    style HR fill:#f66,stroke:#333,stroke-width:2px
    linkStyle 0 stroke:#ff0000,stroke-width:4px,color:red

```
