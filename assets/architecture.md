flowchart TD

    subgraph User["Operator"]
        A1[Runs tool-box]
        A2[Runs individual tools]
    end

    A1 --> IDX

    subgraph IDX["tool-box (Indexer)"]
        I1[Scans /usr/local/bin/bash]
        I2[Scans /usr/local/bin/python]
        I3[Scans /usr/local/bin/php]
        I4[Extracts metadata<br/>Version • Purpose]
        I5[Displays unified tool list]
    end

    IDX -->|Lists tools| User

    A2 -->|Executes| Tools

    subgraph Tools["Toolbox Tools"]
        direction LR

        subgraph Bash["Bash Tools (/usr/local/bin/bash)"]
            B1[update<br/>System update + locate refresh]
            B2[cleanup<br/>System hygiene]
            B3[diag<br/>Diagnostics & health]
            B4[hash<br/>MD5 creation & verification]
            B5[lstnr<br/>Ethical listener]
            B6[mda4w<br/>Windows memory dump wrapper]
            B7[pgsql-session<br/>Session wrapper]
            B8[pgsql-state<br/>Service state checker]
            B9[polkit<br/>Service toggle]
            B10[repsess<br/>Session repair]
            B11[xfer<br/>Safe remote transfer + exec]
        end

        subgraph Python["Python Tools (/usr/local/bin/python)"]
            P1[bf<br/>Pattern-based brute force demonstrator]
            P2[domcon<br/>Domain connectivity checker]
            P3[is<br/>Injection scanner engine]
            P4[zpg<br/>VyOS zone-pair generator]
        end

        subgraph PHP["PHP Tools (/usr/local/bin/php)"]
            PH1[<empty>]
        end
    end

    Tools -->|Produces output| User

    subgraph Docs["Documentation (/docs)"]
        D1[Tool docs]
        D2[Workflows]
        D3[Ethics & philosophy]
        D4[Changelog]
    end

    User -->|Reads| Docs

    subgraph Philosophy["Defensive Principles"]
        E1[Safe execution models]
        E2[No offensive tooling]
        E3[Predictable behaviour]
        E4[Operator clarity]
        E5[Metadata & versioning]
    end

    Philosophy --> Tools
    Philosophy --> IDX
