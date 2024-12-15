from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
SAMPLE_DIGEST = {
    "date": datetime.now().isoformat(),
    "breakthroughs": [
        {
            "title": "Vision-Language Models for RL",
            "summary": "New approach uses vision-language models to give RL agents common sense understanding",
            "key_points": [
                "Integrates VLM knowledge with RL",
                "Reduces training time significantly",
                "Improves generalization to new tasks"
            ],
            "tags": ["RL", "Vision", "Language Models"],
            "source_url": "https://arxiv.org/abs/example",
            "author": "Research Team A"
        }
    ],
    "expert_insights": [
        {
            "title": "The Future of World Models",
            "summary": "Ilya Sutskever discusses the potential of world models in AI systems",
            "tags": ["World Models", "AGI"],
            "source_url": "#",
            "author": "Ilya Sutskever"
        }
    ],
    "learning_paths": [
        {
            "topic": "World Models",
            "prerequisites": ["RL Basics", "Neural Networks", "Attention Mechanisms"],
            "difficulty": "Advanced"
        }
    ]
}

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Learning Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    </head>
    <body class="bg-gray-100">
        <div id="root"></div>
        <script type="text/babel">
            function Dashboard() {
                const [digest, setDigest] = React.useState(null);

                React.useEffect(() => {
                    fetch('/api/digest')
                        .then(res => res.json())
                        .then(data => setDigest(data));
                }, []);

                if (!digest) return <div>Loading...</div>;

                return (
                    <div class="container mx-auto p-6">
                        <h1 class="text-3xl font-bold mb-8">AI Learning Dashboard</h1>
                        
                        <div class="grid grid-cols-1 gap-6">
                            <section>
                                <h2 class="text-2xl font-bold mb-4">Latest Breakthroughs</h2>
                                {digest.breakthroughs.map((item, i) => (
                                    <div key={i} class="bg-white rounded-lg shadow p-6 mb-4">
                                        <div class="flex gap-2 mb-2">
                                            {item.tags.map((tag, j) => (
                                                <span key={j} class="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm">
                                                    {tag}
                                                </span>
                                            ))}
                                        </div>
                                        <h3 class="text-xl font-semibold mb-2">{item.title}</h3>
                                        <p class="text-gray-600 mb-4">{item.summary}</p>
                                        <ul class="list-disc pl-5 mb-4">
                                            {item.key_points.map((point, j) => (
                                                <li key={j} class="text-gray-700">{point}</li>
                                            ))}
                                        </ul>
                                        <div class="flex gap-4">
                                            <a href={item.source_url} class="text-blue-600 hover:text-blue-800">
                                                Source →
                                            </a>
                                        </div>
                                    </div>
                                ))}
                            </section>

                            <section>
                                <h2 class="text-2xl font-bold mb-4">Expert Insights</h2>
                                {digest.expert_insights.map((item, i) => (
                                    <div key={i} class="bg-white rounded-lg shadow p-6 mb-4">
                                        <div class="flex gap-2 mb-2">
                                            {item.tags.map((tag, j) => (
                                                <span key={j} class="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                                                    {tag}
                                                </span>
                                            ))}
                                        </div>
                                        <h3 class="text-xl font-semibold mb-2">{item.title}</h3>
                                        <p class="text-gray-600 mb-4">{item.summary}</p>
                                        <div class="flex gap-4">
                                            <a href={item.source_url} class="text-blue-600 hover:text-blue-800">
                                                Read More →
                                            </a>
                                        </div>
                                    </div>
                                ))}
                            </section>

                            <section>
                                <h2 class="text-2xl font-bold mb-4">Learning Paths</h2>
                                {digest.learning_paths.map((path, i) => (
                                    <div key={i} class="bg-white rounded-lg shadow p-6 mb-4">
                                        <h3 class="text-xl font-semibold mb-2">{path.topic}</h3>
                                        <div class="flex gap-2 mb-4">
                                            {path.prerequisites.map((prereq, j) => (
                                                <span key={j} class="bg-purple-100 text-purple-800 px-2 py-1 rounded text-sm">
                                                    {prereq}
                                                </span>
                                            ))}
                                        </div>
                                        <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                                            Start Learning
                                        </button>
                                    </div>
                                ))}
                            </section>
                        </div>
                    </div>
                );
            }

            ReactDOM.render(<Dashboard />, document.getElementById('root'));
        </script>
    </body>
    </html>
    """

@app.get("/api/digest")
async def get_digest():
    return SAMPLE_DIGEST

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)