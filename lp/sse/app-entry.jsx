/* Smart Study English — App entry */

const SSE_SCROLL_OFFSET = 60;

function sseScrollToSection(id, behavior = "smooth") {
  const el = document.getElementById(id);
  if (!el) return;
  window.scrollTo({ top: el.offsetTop - SSE_SCROLL_OFFSET, behavior });
}

function App() {
  React.useEffect(() => {
    const hash = window.location.hash.replace(/^#/, "");
    if (!hash) return;

    const targetId = hash === "apply" ? "final" : hash;
    sseScrollToSection(targetId, "auto");

    const cleanUrl = window.location.pathname + window.location.search;
    history.replaceState(null, "", cleanUrl);
  }, []);

  return (
    <>
      <StickyLineCTA />
      <Hero />
      <HeroProof />
      <AuthoritySection />
      <EmpathySection />
      <SelfCheckSection />
      <ThreeReasonsSection />
      <BrainCompareSection />
      <WhySection />
      <MethodSection />
      <VoicesSection />
      <RoadmapSection />
      <DaysSection />
      <RoutineSection />
      <SupportFourSection />
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
