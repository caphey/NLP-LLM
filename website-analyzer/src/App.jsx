import { useState, useEffect } from "react";
import HeroSection from "./components/sections/HeroSection";
import SearchSection from "./components/sections/SearchSection";
import FeaturesSection from "./components/sections/FeaturesSection";
import TechnologiesSection from "./components/sections/TechnologiesSection";
import AnalysisResults from "./components/analysis/AnalysisResults";

const App = () => {
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [showResults, setShowResults] = useState(false);
  const [analyzedUrl, setAnalyzedUrl] = useState("");
  const [analysisResults, setAnalysisResults] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async (url) => {
    setAnalyzedUrl(url);
    setIsAnalyzing(true);
    setError(null);

    try {
      const response = await fetch("http://localhost:5000/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: url,
        }),
      });

      const data = await response.json();
      setAnalysisResults(data);
      setShowResults(true);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsAnalyzing(false);
    }
  };

  if (showResults && analysisResults) {
    return (
      <AnalysisResults
        results={analysisResults}
        url={analyzedUrl}
        onBack={() => setShowResults(false)}
      />
    );
  }

  return (
    <div className="min-h-screen bg-black selection:bg-blue-500/20 selection:text-blue-200">
      <div
        className="absolute inset-0"
        style={{
          backgroundImage:
            "radial-gradient(circle at center, rgba(59, 130, 246, 0.1) 2px, transparent 2px)",
          backgroundSize: "24px 24px",
        }}
      ></div>
      <div className="relative container mx-auto px-4 py-16">
        <HeroSection />
        <SearchSection
          onAnalyze={handleAnalyze}
          isAnalyzing={isAnalyzing}
          error={error}
        />
        <FeaturesSection />
        <TechnologiesSection />
      </div>
    </div>
  );
};

export default App;
