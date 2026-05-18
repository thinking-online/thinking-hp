/* Smart Study English — App entry */

function App() {
  return (
    <>
      <StickyLineCTA />
      <Hero />
      <HeroProof />
      <AuthoritySection />
      <EmpathySection />
      <BrainCompareSection />
      <SelfCheckSection />
      <WhySection />
      <MethodSection />
      <VoicesSection />
      <ResultsSection />
      <RoadmapSection />
      <DaysSection />
      <RoutineSection />
      <ProgramContentsSection />
      <PriceSection />
      <GuaranteeSection />
      <MessageSection />
      <ApplyFlowSection />
      <FAQSection />
      <FinalSection />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
