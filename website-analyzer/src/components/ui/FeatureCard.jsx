const FeatureCard = ({ icon, title, description, gradient }) => {
  return (
    <div className="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-lg rounded-2xl p-8 text-white border border-white/10 transform hover:scale-105 transition-all cursor-pointer">
      <div
        className={`bg-blue-500/10 text-blue-400 w-12 h-12 rounded-lg flex items-center justify-center mb-6`}
      >
        {icon}
      </div>
      <h3 className="text-xl font-['Space_Grotesk'] font-bold mb-4">{title}</h3>
      <p className="text-indigo-200 leading-relaxed font-['Inter']">
        {description}
      </p>
    </div>
  );
};

export default FeatureCard;
