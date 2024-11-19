import { useState } from "react";
import { Globe, ArrowRight } from "lucide-react";

const SearchSection = ({ onAnalyze, isAnalyzing, error }) => {
  const [url, setUrl] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (url.trim()) {
      onAnalyze(url);
    }
  };

  return (
    <div className="relative max-w-2xl mx-auto mb-16">
      <div className="absolute -inset-0.5 bg-blue-500 rounded-lg blur opacity-30 group-hover:opacity-100 transition"></div>
      <form onSubmit={handleSubmit} className="relative group">
        <div className="flex justify-start items-center bg-slate-900/80 backdrop-blur-xl rounded-lg p-2 border border-slate-700/50">
          <div className="flex items-center gap-2 px-3 text-slate-400 border-r border-slate-700/50">
            <Globe size={20} className="text-blue-400" />
            <span className="text-sm">https://</span>
          </div>
          <input
            type="url"
            placeholder="Entrez l'URL de votre site web"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="w-full px-4 py-2 bg-transparent text-white focus:outline-none text-md placeholder-slate-500"
            required
          />
          <button
            type="submit"
            disabled={isAnalyzing}
            className="relative bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-all duration-200 flex justify-center gap-3 items-center disabled:opacity-50"
          >
            {isAnalyzing ? (
              <>
                Analyse
                <div className="animate-spin rounded-full h-4 w-4 border-2 border-white/20 border-r-white"></div>
              </>
            ) : (
              <>
                Analyser
                <ArrowRight
                  size={16}
                  className="transition-transform group-hover:translate-x-1"
                />
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchSection;
