import { Code, LineChart, Users } from "lucide-react";

const HeroSection = () => {
  return (
    <div className="text-center mb-16">
      <div className="inline-flex items-center bg-blue-500/10 rounded-full px-3 py-1 text-md text-blue-300 border border-blue-500/20 gap-2 mb-8">
        <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>{" "}
        Analyse avancée par intelligence artificielle
      </div>

      <h1 className="text-6xl font-bold text-white mb-6 font-['Space_Grotesk'] leading-tight tracking-tight">
        Analysez et optimisez votre
        <span className="bg-gradient-to-r from-indigo-400 to-blue-400 text-transparent bg-clip-text">
          {" "}
          présence web
        </span>
      </h1>

      <p className="text-xl text-indigo-200 mb-8 max-w-2xl mx-auto leading-relaxed">
        Une analyse complète de votre site web grâce à nos algorithmes
        d'intelligence artificielle. Obtenez des insights précis et des
        recommandations concrètes.
      </p>

      <div className="flex justify-center gap-4 mb-12">
        <div className="flex items-center bg-white/5 backdrop-blur-lg rounded-full px-4 py-2 text-blue-200 border border-white/10">
          <Code size={20} className="mr-2 text-blue-400" /> Analyse technique
        </div>
        <div className="flex items-center bg-white/5 backdrop-blur-lg rounded-full px-4 py-2 text-blue-200 border border-white/10">
          <LineChart size={20} className="mr-2 text-blue-400" /> SEO avancé
        </div>
        <div className="flex items-center bg-white/5 backdrop-blur-lg rounded-full px-4 py-2 text-blue-200 border border-white/10">
          <Users size={20} className="mr-2 text-blue-400" /> UX & Design
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
