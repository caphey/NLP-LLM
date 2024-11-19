import React, { useState } from "react";
import {
  Globe,
  BarChart2,
  Users,
  Activity,
  ArrowLeft,
  FileText,
  Layout,
  Image,
} from "lucide-react";

const AnalysisResults = ({ results, url, onBack }) => {
  const [activeTab, setActiveTab] = useState("seo_technique");

  const tabs = [
    {
      id: "seo_technique",
      label: "SEO Technique",
      icon: <BarChart2 size={20} />,
    },
    {
      id: "contenu_marketing",
      label: "Contenu Marketing",
      icon: <FileText size={20} />,
    },
    {
      id: "experience_utilisateur",
      label: "UX Design",
      icon: <Layout size={20} />,
    },
    {
      id: "analyse_images",
      label: "Analyse Images",
      icon: <Image size={20} />,
    },
  ];

  const cleanContent = (text) => {
    let cleaned = text
      .replace(/[*#_`~]/g, "")
      .replace(/^[-*+]\s*/gm, "")
      .replace(/^\d+\.\s*/gm, "")
      .replace(/\[\s*\]/g, "")
      .replace(/\(\s*\)/g, "")
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

    let paragraphs = cleaned
      .split(/\n+/)
      .map((p) => p.trim())
      .filter((p) => p.length > 0);

    paragraphs = paragraphs.map((p) => {
      if (p.length < 50 && p.endsWith(":")) {
        return {
          type: "heading",
          content: p.slice(0, -1),
        };
      }
      return {
        type: "paragraph",
        content: p,
      };
    });

    return paragraphs;
  };

  return (
    <div className="min-h-screen bg-black">
      <div className="container mx-auto px-4 py-8">
        {/* Header avec navigation */}
        <button
          onClick={onBack}
          className="mb-8 flex items-center gap-2 px-4 py-2 text-blue-400 hover:text-blue-500 bg-white/5 hover:bg-white/10 rounded-lg transition-colors border border-white/10"
        >
          <ArrowLeft size={20} />
          Retour à l'accueil
        </button>

        {/* Titre et URL */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center bg-blue-500/10 rounded-full px-3 py-1 text-md text-blue-300 border border-blue-500/20 gap-2 mb-8">
            <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>{" "}
            Rapport d'analyse détaillé
          </div>
          <h1 className="text-4xl font-bold text-white mb-6 font-['Space_Grotesk']">
            Analyse complète de votre site
          </h1>
        </div>

        <div className="flex items-center bg-slate-900/80 backdrop-blur-xl rounded-lg border border-slate-700/50 mb-8 gap-3 p-4">
          <Globe size={20} className="text-blue-400" />
          <span className="text-blue-300">URL analysée :</span>
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:text-blue-300 transition-colors overflow-hidden overflow-ellipsis"
          >
            {url}
          </a>
        </div>

        {/* KPI Cards */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <KPICard
            title="Performance"
            score={results.kpi_overview.performance.score}
            label={results.kpi_overview.performance.label}
            icon={<BarChart2 />}
          />
          <KPICard
            title="Expérience Utilisateur"
            score={results.kpi_overview.user_experience.score}
            label={results.kpi_overview.user_experience.label}
            icon={<Users />}
          />
          <KPICard
            title="Marketing"
            score={results.kpi_overview.marketing.score}
            label={results.kpi_overview.marketing.label}
            icon={<Activity />}
          />
        </div>

        {/* Navigation Tabs */}
        <div className="grid grid-cols-4 gap-4 mb-8">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center justify-center gap-3 p-4 rounded-xl backdrop-blur-lg border transition-all duration-200
                ${
                  activeTab === tab.id
                    ? "bg-blue-400/20 border-white/20 text-white"
                    : "bg-white/5 border-white/10 text-indigo-300 hover:bg-white/10 hover:text-indigo-200"
                }`}
            >
              {tab.icon}
              <span className="font-medium font-['Space_Grotesk']">
                {tab.label}
              </span>
            </button>
          ))}
        </div>

        {/* Content Section */}
        <div className="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-lg rounded-xl border border-white/10 overflow-hidden p-8">
          {Object.entries(results.detailed_analysis)
            .filter(([key]) => key === activeTab)
            .map(([key, section]) => (
              <div key={key}>
                <h3 className="text-2xl font-bold text-white mb-6 font-['Space_Grotesk']">
                  {section.title}
                </h3>
                <div className="space-y-6">
                  {cleanContent(section.content).map((item, index) => (
                    <div
                      key={index}
                      className={`${
                        item.type === "heading"
                          ? "text-xl font-semibold text-white mb-2"
                          : "text-indigo-200 leading-relaxed"
                      }`}
                    >
                      {item.content}
                    </div>
                  ))}
                </div>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
};

const KPICard = ({ title, score, label, icon }) => {
  const ringColor =
    score >= 80
      ? "text-pink-400"
      : score >= 60
      ? "text-blue-400"
      : "text-indigo-400";

  return (
    <div
      className={`bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-lg rounded-2xl p-8 text-white border border-white/10 transform hover:scale-105 transition-all cursor-pointe`}
    >
      <div className="flex items-center gap-4 mb-6">
        <div className={`p-2 rounded-lg bg-blue-500/10 text-blue-400`}>
          {React.cloneElement(icon, { size: 24 })}
        </div>
        <h4 className="text-lg font-semibold text-white font-['Space_Grotesk']">
          {title}
        </h4>
      </div>

      <div className="flex items-center gap-4">
        <div className="relative">
          <svg className="w-20 h-20">
            <circle
              className="text-white/5"
              strokeWidth="8"
              stroke="currentColor"
              fill="transparent"
              r="32"
              cx="40"
              cy="40"
            />
            <circle
              className={ringColor}
              strokeWidth="8"
              strokeDasharray={`${score * 2.01} 200`}
              strokeLinecap="round"
              stroke="currentColor"
              fill="transparent"
              r="32"
              cx="40"
              cy="40"
              style={{
                transformOrigin: "50% 50%",
                transform: "rotate(-90deg)",
                transition: "stroke-dasharray 0.5s ease",
              }}
            />
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-2xl font-bold text-white">{score}</span>
          </div>
        </div>
        <p className="text-sm text-indigo-200 flex-1">{label}</p>
      </div>
    </div>
  );
};

export default AnalysisResults;
