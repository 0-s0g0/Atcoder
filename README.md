graph TD
    %% ARグラス側
    subgraph AR_グラス_ユーザー側
        A[カメラ映像キャプチャ] --> B[ARグラス内処理/レンダリング]
        B -- ARオーバーレイ表示 --> C(ユーザー視界)
        B -- 映像データ送信 (SDK/通信) --> D(ネットワーク通信層)
    end

    %% ネットワークとAWSエッジ
    subgraph ネットワーク_および_AWSエッジ
        D -- Wi-Fi/5G/LTE --> E[インターネット/VPN]
        E -- 映像ストリーム転送 --> F[エッジデバイス/ゲートウェイ (オプション)]
        F -- 映像データ前処理/圧縮 --> G[AWS Kinesis Video Streams]
    end

    %% AWSクラウド
    subgraph AWSクラウド
        subgraph AI推論エンジン
            H[AWS Lambda (KVS Processor)] -- フレーム抽出/整形 --> I(FastAPIサーバー on EC2)
            I -- モデルロード/推論実行 --> J[学習済みモデル (S3からロード)]
            I -- 推論結果送信 --> K(推論結果格納サービス)
        end

        K -- 結果取得/集約 --> L[AWS Lambda (ARオーバーレイ計算)]
        L -- ARオーバーレイ情報送信 --> M[AWS IoT Core/WebSockets]
    end

    %% フィードバックとデータ保存
    subgraph リアルタイムフィードバック
        M -- リアルタイム通信 --> D
    end

    subgraph データ永続化_と_学習
        K --> N[AWS DynamoDB/Redis]
        J -- モデルソース --> O[AWS S3 (学習データ/モデルリポジトリ)]
        P[AWS SageMaker (モデル学習)] -- 学習済みモデル保存 --> O
    end

    %% 補助関係
    G -- 映像データイベント --> H
    L -- 結果取得 --> N

    %% スタイル
    style A fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style B fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style C fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style D fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style F fill:#e0f2f7,stroke:#26c6da,stroke-width:2px
    style G fill:#b2ebf2,stroke:#00acc1,stroke-width:2px
    style H fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style I fill:#fff8e1,stroke:#ffd54f,stroke-width:2px
    style J fill:#f8bbd0,stroke:#d81b60,stroke-width:2px
    style K fill:#ffe0b2,stroke:#ffb74d,stroke-width:2px
    style L fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style M fill:#b2ebf2,stroke:#00acc1,stroke-width:2px
    style N fill:#ffe0b2,stroke:#ffb74d,stroke-width:2px
    style O fill:#f8bbd0,stroke:#d81b60,stroke-width:2px
    style P fill:#f8bbd0,stroke:#d81b60,stroke-width:2px
