# -*- coding: utf-8 -*-
"""Interactive megacodes: Neonatal Resuscitation 2025.

Every setting, dose and target is taken from this module's Appendix E (2025 AHA/AAP Part 5, ILCOR 2025):
  PPV: 21% at >=35 wk, 21-30% at 32-34 wk, >=30% may be considered below 32 wk | rate 30-60/min | PIP 25 (20-25 preterm) | PEEP 5
  max face-mask pressure 40 cm H2O term, 30 preterm | CPAP 5-6, never above 8 | compressions 3:1 with FiO2 100%
  epinephrine IV/IO 0.02 mg/kg of 0.1 mg/mL (0.2 mL/kg) + 3 mL flush; ET 0.1 mg/kg (1 mL/kg) only without IV/IO
  volume 10 mL/kg over 5-10 min | pre-ductal SpO2 targets 2/3/4/5/10 min: 65-70/70-75/75-80/80-85/85-95%
  temperature 36.5-37.5 C | cooling: refer within the 6-hour window, never improvise.
Compile with:  python megacodes/make.py
"""

def O(t, fb, ok=False, to=None, dt=0, crit=False, mark=None, mt=None):
    o = {"t": t, "fb": fb, "dt": dt}
    if ok: o["ok"] = 1
    if crit: o["crit"] = 1
    if to: o["to"] = to
    if mark: o["mark"] = mark
    if mt is not None: o["mt"] = mt
    return o

def N(text, ask, opts, **mon):
    return {"text": text, "ask": ask, "opts": opts, "mon": mon}

def E(kind, text, **mon):
    return {"end": kind, "text": text, "mon": mon}

INTRO = ("Six branching cases at the radiant warmer, played one decision at a time against the clock since birth. "
         "Wrong calls change the baby, cost seconds, or are flagged as critical errors, and every choice is explained. "
         "The options are shuffled on every run. A case opens when its Part opens. <b>Practice only:</b> results appear in "
         "your completion record and your faculty's class report, but they are not part of the certificate. Hands-on "
         "simulation with a doll and your own equipment (Appendix B) is still essential.")

NEO = ["hr", "spo2", "fio2"]

CASES = [

# ---------------------------------------------------------------- 1 · flat term baby
{
 "id": "n-flat", "title": "The unexpectedly flat baby", "patient": "39 weeks · about 3.2 kg · clear liquor · one attendant",
 "part": "C", "units": [7, 10, 12, 13], "minutes": 4, "monitor": NEO, "clockLabel": "Since birth",
 "brief": "An uncomplicated labour at 39 weeks. You are the only attendant at the birth; a nurse is in the next room.",
 "start": "n1",
 "nodes": {
  "n1": N("<p>He is born limp and pale, and he is not breathing.</p>", "What do you do in the first 30 seconds?", [
     O("Call for help; clamp (intact cord milking is reasonable if it causes no delay) and move him to the warmer; dry, stimulate, position the airway, and clear it only if obstructed.",
       "A non-vigorous baby goes to the warmer. The initial steps take about 30 seconds, and cord management must never delay ventilation.", ok=True, to="n2", dt=30, mark="init"),
     O("Routine deep suction of the mouth, nose and pharynx.",
       "Routine suction is not recommended. Clear the airway only if it is obstructed; deep suction can cause bradycardia.", dt=20),
     O("Hold him upside down and slap his back and soles repeatedly.",
       "Vigorous or painful stimulation is harmful. Gentle drying and rubbing the back or soles is enough; if he does not respond, ventilate.", crit=True, dt=20),
     O("Keep him on his mother's abdomen with the cord intact for 3 minutes of deferred clamping.",
       "Deferred clamping is for babies who do not need resuscitation. Cord management must never delay ventilation.", crit=True, dt=60),
   ], hr=None, spo2=None, fio2="21"),
  "n2": N("<p>After drying and stimulation he is still apnoeic and limp. Heart rate by stethoscope: 70/min (7 beats in 6 seconds).</p>",
          "What now?", [
     O("Start PPV by mask now: 21% oxygen, 30–60 breaths/min, PIP about 25 cm H₂O with PEEP 5; put the oximeter on the right hand or wrist; shout again for help.",
       "Apnoea, or HR below 100/min, after the initial steps means PPV, and the aim is to start within 60 seconds of birth. Term babies start in 21%.", ok=True, to="n3", dt=20, mark="ppv"),
     O("Stimulate for another 30 seconds.",
       "Stimulation has already failed. Every extra second of apnoea deepens the hypoxia; the golden minute is for ventilation.", crit=True, to="n2x", dt=30),
     O("Free-flow 100% oxygen to the face.",
       "Free-flow oxygen does nothing for an apnoeic baby: he needs breaths. Term babies start PPV in 21% oxygen.", dt=30),
     O("Go to fetch the senior doctor, then start ventilation.",
       "Call for help while you ventilate. Leaving an apnoeic baby alone loses the golden minute.", crit=True, to="n2x", dt=60),
   ], hr=70, spo2=None, fio2="21", flag="Apnoeic"),
  "n2x": N("<p>Thirty more seconds pass. The heart rate is now 50/min.</p>", "What now?", [
     O("Start mask PPV in 21% at once, with PIP about 25 and PEEP 5.", "Yes: ventilation, now. It is the treatment for almost every baby who needs resuscitation.", ok=True, to="n3", dt=20, mark="ppv"),
     O("More stimulation.", "Stimulation has failed twice. Ventilate.", dt=20),
     O("Free-flow 100% oxygen.", "An apnoeic baby needs breaths, not free-flow oxygen.", dt=20),
   ], hr=50, spo2=None, fio2="21", flag="Apnoeic"),
  "n3": N("<p>You are ventilating by mask, but the chest is not moving and the heart rate is not rising: 60/min.</p>",
          "What do you do?", [
     O("Corrective steps, announced aloud: <b>M</b>, re-apply the mask to improve the seal; <b>R</b>, reposition the head in the sniffing position.",
       "MR SOPA starts with the mask and the head position, which fix most failures. Say each step aloud so the team knows where you are.", ok=True, to="n4", dt=20, mark="mr"),
     O("Go straight to 40 cm H₂O.",
       "Raising the pressure before fixing the seal and the airway position is the wrong order. M and R come first; P is the fifth step.", dt=20),
     O("Start chest compressions: the HR is 60.",
       "Compressions start only after 30 seconds of ventilation that moves the chest. Here, ineffective ventilation is the problem.", crit=True, dt=30),
     O("Intubate straight away.",
       "An alternative airway is step A, after M, R, S, O and P, unless those fail. Most failures are fixed with the mask and head position.", dt=60),
   ], hr=60, spo2=None, fio2="21", flag="Chest NOT moving"),
  "n4": N("<p>After the mask is re-applied and the head repositioned, the chest rises with each breath. Heart rate 90/min and rising. SpO₂ is 68% at 2 minutes.</p>",
          "What next?", [
     O("Continue effective PPV for 30 seconds, keep FiO₂ at 21% (SpO₂ is within the 2-minute target), and reassess the heart rate.",
       "Effective ventilation is working. At 2 minutes the target is 65–70%, so no extra oxygen is needed.", ok=True, to="n5", dt=45),
     O("Increase the oxygen to 100% to get SpO₂ above 90%.",
       "At 2 minutes the target is 65–70%. Hyperoxia harms newborns: titrate to the minute-by-minute targets, not to adult values.", dt=20),
     O("Stop ventilating: the heart rate is above 60.",
       "Stop only when HR is above 100/min <i>and</i> breathing is sustained. At 90/min and apnoeic, he still needs PPV.", crit=True, dt=20),
   ], hr=90, spo2=68, fio2="21", flag="Chest moving", target="Target SpO₂ at 2 min: 65–70%"),
  "n5": N("<p>At 3½ minutes: HR 130/min, irregular breaths starting, SpO₂ 78%.</p>", "What next?", [
     O("Continue PPV while breathing becomes established, gradually reducing the rate; stop when breathing is sustained and HR stays above 100; then monitor him with oximetry, temperature and a glucose plan.",
       "Wean rather than stop abruptly. A baby who needed PPV needs post-resuscitation observation.", ok=True, to="end", dt=120),
     O("Stop PPV straight away: the heart rate is over 100.",
       "Stopping on one criterion often causes apnoea again within a minute. Wait until breathing is sustained, then wean.", dt=30),
     O("Intubate to secure the airway now that he is better.", "There is no indication: ventilation is effective and he is starting to breathe.", dt=60),
   ], hr=130, spo2=78, fio2="21", flag="Breathing", target="Target SpO₂ at 4 min: 75–80%"),
  "end": E("good", "<p>By 6 minutes he is crying: HR 145/min, SpO₂ 86% in air. He goes skin-to-skin with his mother under close observation, with oximetry, temperature (36.5–37.5 °C) and glucose monitoring.</p>",
           hr=145, spo2=86, fio2="21", target="Target SpO₂ at 5 min: 80–85%"),
 },
 "timers": [{"mark": "ppv", "label": "PPV started", "target": "within 60 s of birth", "max": 60}],
 "debrief": ["A limp, apnoeic baby goes to the warmer: cord management must not delay ventilation.",
             "The initial steps take about 30 seconds: no routine suction and no vigorous stimulation.",
             "Apnoea, or HR below 100/min, after the initial steps: start PPV within 60 seconds of birth, in 21% for term babies.",
             "Chest not moving: MR SOPA in order, announced aloud. No compressions until ventilation is effective.",
             "Stop PPV only when HR is above 100/min and breathing is sustained. Titrate oxygen to the minute-by-minute SpO₂ targets."],
},

# ---------------------------------------------------------------- 2 · meconium
{
 "id": "n-mec", "title": "Thick meconium, non-vigorous baby", "patient": "40 weeks · about 3.4 kg · thick meconium-stained liquor",
 "part": "C", "units": [7, 13, 14], "minutes": 4, "monitor": NEO, "clockLabel": "Since birth",
 "brief": "Thick meconium-stained liquor at 40 weeks. You are at the warmer with a senior nurse.",
 "start": "n1",
 "nodes": {
  "n1": N("<p>The baby is born limp and apnoeic, covered in thick meconium. The senior nurse reaches for the laryngoscope to suction the trachea before the first breath.</p>",
          "What do you do?", [
     O("No routine intubation for suction: take him to the warmer, do the initial steps (clear the mouth and nose only if obstructed), and start PPV within 60 seconds if he is still apnoeic.",
       "Routine tracheal suction of non-vigorous babies with meconium was abandoned: randomised trials showed no benefit, and it delays ventilation.", ok=True, to="n2", dt=30, mark="init"),
     O("Intubate and suction the trachea before any breath: the meconium is thick.",
       "Trials in non-vigorous meconium-stained babies found no benefit from routine tracheal suction, and it delays ventilation. Suction the trachea only if the airway is obstructed.", dt=60),
     O("Suction the mouth and nose deeply while the head is on the perineum.",
       "Intrapartum suctioning is not recommended, and deep suctioning can cause bradycardia.", dt=20),
   ], hr=None, spo2=None, fio2="21"),
  "n2": N("<p>He is still apnoeic after the initial steps. Heart rate 80/min.</p>", "What now?", [
     O("Start mask PPV in 21% at 30–60 breaths/min, PIP about 25, PEEP 5, and put the oximeter on the right wrist.",
       "Meconium does not change the indication or the settings for PPV.", ok=True, to="n3", dt=30, mark="ppv", mt=5),
     O("Now intubate and suction before ventilating.", "PPV comes first. Tracheal suction is only for suspected obstruction once ventilation has failed.", dt=60),
     O("Stimulate for another 30 seconds.", "The initial steps have failed; the golden minute is for ventilation.", crit=True, dt=30),
   ], hr=80, spo2=None, fio2="21", flag="Apnoeic"),
  "n3": N("<p>Despite a good mask seal, repositioning, suctioning the mouth and nose, opening the mouth, and raising the pressure step by step to 40 cm H₂O, the chest still does not move. Thick meconium is visible in the mouth.</p>",
          "What next?", [
     O("Alternative airway: intubate. If thick meconium is obstructing the trachea, suction it through the tube with a meconium aspirator, then ventilate.",
       "This is the exception: airway obstruction despite MR SOP. Tracheal suction can clear it.", ok=True, to="n4", dt=60, mark="airway"),
     O("Start chest compressions: the HR is 70.", "Compressions come only after 30 seconds of <i>effective</i> ventilation. The chest is not moving yet.", crit=True, dt=30),
     O("Increase the mask pressure to 60 cm H₂O.",
       "The maximum face-mask pressure for a term baby is 40 cm H₂O. Higher pressure risks a pneumothorax and will not clear an obstruction.", crit=True, dt=30),
   ], hr=70, spo2=None, fio2="21", flag="Chest NOT moving"),
  "n4": N("<p>Meconium is suctioned from the trachea. With ventilation through the tube the chest now rises, and the heart rate climbs to 120/min. SpO₂ 72% at 3 minutes.</p>",
          "What next?", [
     O("Continue ventilation, titrate oxygen to the targets, watch for a pneumothorax and pulmonary hypertension, and plan NICU admission.",
       "Meconium aspiration can cause pneumothorax and persistent pulmonary hypertension, so he needs close monitoring.", ok=True, to="end", dt=120),
     O("Give 100% oxygen for an hour to prevent pulmonary hypertension.", "Titrate to the SpO₂ targets: both hypoxia and hyperoxia are harmful.", dt=30),
     O("Wash out the lungs with saline through the tube.", "Saline lavage is not a resuscitation step and is not recommended.", dt=30),
   ], hr=120, spo2=72, fio2="21", flag="Chest moving", target="Target SpO₂ at 3 min: 70–75%"),
  "end": E("good", "<p>He is admitted to the NICU on CPAP. The chest X-ray shows meconium aspiration without a pneumothorax.</p>",
           hr=148, spo2=90, fio2="30", target="Target SpO₂ at 10 min: 85–95%"),
 },
 "timers": [{"mark": "ppv", "label": "PPV started", "target": "within 60 s of birth", "max": 60}],
 "debrief": ["Meconium does not change the first steps: the warmer, the initial steps, and PPV within 60 seconds if needed.",
             "No routine intubation for tracheal suction in non-vigorous babies: randomised trials showed no benefit.",
             "Intubate and suction only when ventilation fails because of suspected airway obstruction.",
             "The maximum face-mask pressure for a term baby is 40 cm H₂O.",
             "After meconium aspiration, watch for a pneumothorax and pulmonary hypertension."],
},

# ---------------------------------------------------------------- 3 · full arrest, abruption
{
 "id": "n-arrest", "title": "Full arrest after abruption", "patient": "36 weeks · about 2.5 kg · caesarean for abruption",
 "part": "D", "units": [14, 15, 16, 17], "minutes": 6, "monitor": ["rhythm"] + NEO, "clockLabel": "Since birth",
 "brief": "Emergency caesarean section under general anaesthesia at 36 weeks, for placental abruption with fetal bradycardia. Your team of three is at the warmer.",
 "start": "n1",
 "nodes": {
  "n1": N("<p>The baby is limp, pale and apnoeic. Heart rate 40/min by stethoscope.</p>", "What do you do first?", [
     O("Quick initial steps, then PPV within 60 seconds: 21% (she is ≥35 weeks), PIP about 25, PEEP 5; call for more help; oximeter on the right wrist.",
       "Ventilation comes first in the newborn, even with a heart rate of 40/min.", ok=True, to="n2", dt=60, mark="ppv", mt=20),
     O("Start chest compressions immediately: the HR is 40.",
       "Ventilation comes first. Compressions start only after 30 seconds of ventilation that moves the chest, preferably through an alternative airway.", crit=True, dt=30),
     O("Free-flow 100% oxygen and more stimulation.", "An apnoeic baby needs breaths, not free-flow oxygen or more stimulation.", dt=30),
   ], rhythm="none", hr=40, spo2=None, fio2="21", flag="Apnoeic"),
  "n2": N("<p>After mask adjustment and repositioning, the chest is moving well. After 30 seconds of effective ventilation the heart rate is still 40/min.</p>",
          "What next?", [
     O("Insert an alternative airway (tracheal tube or laryngeal mask), confirm it with a CO₂ detector, and go straight on to compressions.",
       "HR is still below 60/min after 30 seconds of effective ventilation, so compressions are indicated. NRP recommends placing an alternative airway first if you have not already, because it keeps ventilation reliable while you compress. No further 30-second wait is needed.", ok=True, to="n3", dt=45, mark="airway"),
     O("Start compressions now, ventilating through the face mask.",
       "Acceptable if an airway cannot be placed quickly, but with a skilled team present an alternative airway first makes ventilation more reliable during compressions.", dt=20),
     O("Increase the ventilation rate to 100 breaths/min.",
       "The rate is 30–60/min (30/min during compressions). Faster rates do not help and can cause air trapping.", dt=30),
   ], rhythm="none", hr=40, spo2=None, fio2="21", flag="Chest moving"),
  "n3": N("<p>The tracheal tube is in, the CO₂ detector changes colour, and the chest is moving. The heart rate is still 40/min. ECG leads are now attached.</p>",
          "What now, and who does what?", [
     O("Start compressions (two-thumb, lower third of the sternum, one-third of the chest depth) at 3:1, 90 compressions and 30 breaths a minute; increase FiO₂ to 100%; at the same time one person places an emergency UVC and another prepares epinephrine.",
       "HR below 60/min despite 30 seconds of effective ventilation: compressions at 3:1 with 100% oxygen. Work in parallel so that access and epinephrine are ready by the 60-second check.", ok=True, to="n4", dt=60, mark="cc", mt=5),
     O("Compressions at 15:2, as in older children.",
       "Newborns get 3:1: 90 compressions and 30 breaths a minute, because the problem is almost always ventilation.", dt=20),
     O("Compressions at 3:1 but keep FiO₂ at 21%.",
       "Once compressions start, raise the oxygen to 100% until HR is above 60/min and the oximeter reads reliably.", dt=20),
     O("Compress first, and think about access once you see whether compressions work.",
       "Serial thinking loses minutes. Access and epinephrine should be ready by the time of the 60-second check.", dt=60),
   ], rhythm="brady", hr=40, spo2=None, fio2="21", flag="Tube confirmed"),
  "n4": N("<p>After 60 seconds of coordinated compressions and ventilation, the heart rate is 40/min. The UVC is in and blood aspirates freely.</p>",
          "Which drug, dose and route?", [
     O("Epinephrine 0.05 mg IV via the UVC (0.02 mg/kg = 0.5 mL of 0.1 mg/mL), then a 3 mL saline flush; repeat every 3–5 minutes while HR stays below 60/min.",
       "IV epinephrine 0.02 mg/kg of 0.1 mg/mL, the only concentration used in neonatal resuscitation.", ok=True, to="n5", dt=60, mark="epi1", mt=5),
     O("0.5 mL of 1 mg/mL epinephrine.",
       "That is 0.5 mg, ten times the dose. Only 0.1 mg/mL is used in neonatal resuscitation; say the concentration aloud.", crit=True, dt=30),
     O("Epinephrine 2.5 mL (0.1 mg/kg) of 0.1 mg/mL down the tube, even though the UVC is in.",
       "The tracheal dose (0.1 mg/kg) is for when there is no IV or IO access. With a working UVC, use the IV dose of 0.02 mg/kg.", dt=30),
     O("Sodium bicarbonate 2 mEq/kg.",
       "Not recommended: it can worsen intracellular acidosis and raises the risk of IVH in preterm babies. Treat the cause.", dt=30),
   ], rhythm="brady", hr=40, spo2=None, fio2="100", flag="Compressions in progress"),
  "n5": N("<p>One minute after the epinephrine the heart rate is 50/min. She is very pale, capillary refill 5 seconds, pulses weak. The abruption was large.</p>",
          "What now?", [
     O("Volume: 25 mL (10 mL/kg) of normal saline, or O Rh-negative red cells if severe anaemia is suspected, over 5–10 minutes through the UVC; continue compressions and ventilation.",
       "Pallor, weak pulses and an abruption mean blood loss, and volume is the treatment.", ok=True, to="n6", dt=300, mark="vol", mt=10),
     O("A second dose of epinephrine now, and nothing else.",
       "Pallor, weak pulses and an abruption point to blood loss. Epinephrine will not work without volume.", dt=180),
     O("Push 25 mL of saline as fast as possible.",
       "Give volume over 5–10 minutes, and more slowly in preterm babies. Fast pushes are linked to intraventricular haemorrhage.", dt=30),
     O("Recheck the tube position and change nothing else.",
       "Checking ventilation is always right, but it is working (CO₂ detector, chest movement). The unsolved problem is hypovolaemia.", dt=60),
   ], rhythm="brady", hr=50, spo2=None, fio2="100", flag="Pale · CRT 5 s"),
  "n6": N("<p>During the volume infusion the heart rate climbs to 110/min and her colour improves. The oximeter now reads 80%.</p>",
          "What next?", [
     O("Stop compressions (HR is above 60); continue ventilation; wean oxygen by oximetry; then post-resuscitation care: glucose, temperature, an HIE assessment against the cooling criteria, and a talk with the parents.",
       "Compressions stop once HR is above 60/min. Every baby after a resuscitation like this is assessed for therapeutic hypothermia.", ok=True, to="end", dt=180),
     O("Keep compressing for another minute to be safe.", "Compressions stop once HR is above 60/min; continuing reduces the heart's own output.", dt=30),
     O("Keep FiO₂ at 100% for an hour after the arrest.",
       "Once HR is above 60/min and the oximeter reads reliably, titrate the oxygen down to the targets. Hyperoxia after asphyxia adds injury.", dt=30),
   ], rhythm="sinus", hr=110, spo2=80, fio2="100", flag="HR > 60"),
  "end": E("good", "<p>She is admitted to the NICU. At 1 hour she has moderate encephalopathy, meets the criteria for therapeutic hypothermia, and is cooled within 6 hours of birth.</p>",
           rhythm="sinus", hr=138, spo2=92, fio2="30"),
 },
 "timers": [{"mark": "ppv", "label": "PPV started", "target": "within 60 s of birth", "max": 60},
            {"mark": "epi1", "label": "First epinephrine", "target": "after 60 s of coordinated compressions"}],
 "debrief": ["Ventilation is the treatment in almost every newborn resuscitation. Compressions only after 30 seconds of effective ventilation, ideally through an alternative airway.",
             "Compressions at 3:1 with 100% oxygen. Run access and epinephrine in parallel, not one after the other.",
             "Epinephrine IV 0.02 mg/kg of 0.1 mg/mL (the only concentration), then a 3 mL flush. Tracheal 0.1 mg/kg only if there is no IV or IO access.",
             "No response, pallor and a history of blood loss: give volume, 10 mL/kg over 5–10 minutes.",
             "After ROSC: stop compressions once HR is above 60/min, titrate oxygen, check glucose and temperature, and assess for therapeutic hypothermia."],
},

# ---------------------------------------------------------------- 4 · preterm 28 weeks
{
 "id": "n-preterm", "title": "The 28-week baby", "patient": "28 weeks · about 1.1 kg · four minutes' warning",
 "part": "E", "units": [6, 9, 19], "minutes": 5, "monitor": NEO + ["temp"], "clockLabel": "Clock",
 "brief": "Preterm labour at 28 weeks. Delivery is expected in about 4 minutes, and you are setting up the warmer.",
 "start": "n0",
 "nodes": {
  "n0": N("<p>Delivery is 4 minutes away.</p>", "Which preparation is complete and correct?", [
     O("Room at 23–25 °C, warmer preheated, thermal mattress activated, polyethylene wrap and hat ready, T-piece tested (PIP 20–25, PEEP 5), blender at about 30%, oximeter ready, size 0 blade and 2.5 and 3.0 tubes.",
       "This is the preterm set-up: the thermal bundle, a device that gives PEEP and CPAP, a blender, and the right airway sizes.", ok=True, to="n1", dt=180),
     O("Warm towels to dry her thoroughly; room temperature does not matter under a warmer.",
       "Below 32 weeks the thermal bundle is: room at 23–25 °C, a thermal mattress, and wrapping without drying. Radiant heat alone is not enough.", dt=60),
     O("A self-inflating bag with 100% oxygen for CPAP.",
       "A self-inflating bag cannot give CPAP or reliable PEEP: use a T-piece. Below 32 weeks, 2025 allows starting at 30% or more (30–100% is acceptable); this module starts at about 30% and titrates.", dt=60),
   ], hr=None, spo2=None, fio2=None, temp=None),
  "n1": N("<p>She is born with some tone and irregular breaths. The cord is managed as planned, and she comes to the warmer.</p>", "What do you do first at the warmer?", [
     O("Without drying her, place her in the polyethylene wrap up to the neck, put the hat on, position the airway, and put the oximeter on the right wrist.",
       "Below 32 weeks: wrap without drying. It is the most effective single step against heat loss.", ok=True, to="n2", dt=60, mark="wrap", mt=10),
     O("Dry her thoroughly, then wrap her.", "Below 32 weeks, do not dry the body: wrap her wet. Drying first loses heat and time.", dt=40),
     O("Weigh and measure her before anything else.", "Weighing can wait. Heat loss in the first minutes is what harms her.", dt=60),
   ], hr=140, spo2=None, fio2="30", temp=None, flag="Some tone · irregular breaths"),
  "n2": N("<p>At 2 minutes she is breathing, with a heart rate of 140/min, marked recession and grunting. SpO₂ 55%.</p>",
          "What support does she need?", [
     O("CPAP 5–6 cm H₂O with the T-piece, titrating FiO₂ up from 30% to reach the target range.",
       "She is breathing with HR above 100/min but working hard: CPAP, not PPV. Titrate oxygen to the minute-by-minute targets.", ok=True, to="n3", dt=240, mark="cpap", mt=10),
     O("Start PPV at 25/5.", "PPV is for apnoea, gasping or HR below 100/min. She is breathing with HR 140/min: CPAP first.", dt=60),
     O("Free-flow oxygen through the mask of a self-inflating bag.",
       "The mask of a self-inflating bag does not reliably deliver free-flow oxygen, and the bag cannot give CPAP. Use the T-piece.", dt=60),
     O("Intubate and give surfactant straight away.",
       "CPAP is the first-line support for a breathing preterm baby. Intubation is for CPAP failure or the need for PPV.", dt=120),
   ], hr=140, spo2=55, fio2="30", temp=None, flag="Recession · grunting", target="Target SpO₂ at 2 min: 65–70%"),
  "n3": N("<p>At 6 minutes, on CPAP 6 cm H₂O with FiO₂ 40%: SpO₂ 88% and rising, and the recession is easing.</p>", "What do you do with the oxygen?", [
     O("Reduce FiO₂ step by step, keeping SpO₂ within the target range for her age in minutes.",
       "She is at or slightly above the target for 6 minutes and rising, so wean. Preterm babies are especially vulnerable to hyperoxia.", ok=True, to="n4", dt=240, mark="wean"),
     O("Keep FiO₂ at 40%: better too high than too low.",
       "Leaving FiO₂ high will push SpO₂ to 98% or more. Hyperoxia in preterm babies is linked to retinopathy and lung injury. Titrate.", dt=60),
     O("Increase to 100% to reach 95% quickly.", "That is the wrong direction: she is already at or above target and rising. Hyperoxia harms preterm babies.", crit=True, dt=60),
   ], hr=150, spo2=88, fio2="40", temp=None, target="Target SpO₂ at 5 min: 80–85%; at 10 min: 85–95%"),
  "n4": N("<p>At 10 minutes she is stable on CPAP 6 with FiO₂ 30%, SpO₂ 90%. Axillary temperature 36.2 °C. The NICU is on another floor.</p>",
          "What do you do before and during the transfer?", [
     O("Transfer her on CPAP in a prewarmed incubator, bring her temperature into 36.5–37.5 °C and recheck it, start a glucose plan (IV dextrose), and update the parents.",
       "Normal temperature, glucose and a safe transfer are part of stabilisation.", ok=True, to="end", dt=300),
     O("Her temperature is close enough: carry her in a towel in a nurse's arms.",
       "36.2 °C is hypothermia for her. Transfer in a prewarmed incubator and recheck the temperature.", crit=True, dt=60),
     O("Feed her orally before the transfer to prevent hypoglycaemia.", "A 28-week baby on CPAP cannot feed orally. Start IV dextrose and a glucose plan.", dt=60),
   ], hr=150, spo2=90, fio2="30", temp="36.2", flag="Temp low", target="Target SpO₂ at 10 min: 85–95%"),
  "end": E("good", "<p>She arrives in the NICU at 36.8 °C on CPAP 6 with FiO₂ 28%. Her glucose is 3.4 mmol/L on an IV dextrose infusion.</p>",
           hr=148, spo2=91, fio2="28", temp="36.8"),
 },
 "timers": [{"mark": "wrap", "label": "Wrapped without drying", "target": "on arrival at the warmer"},
            {"mark": "cpap", "label": "CPAP started", "target": "when laboured breathing is seen"}],
 "debrief": ["Below 32 weeks, the thermal bundle: room at 23–25 °C, preheated warmer, thermal mattress, wrap without drying, hat.",
             "Breathing with HR above 100/min but labouring: CPAP 5–6 cm H₂O from a device that can deliver it (T-piece), not PPV.",
             "Below 32 weeks, start at about 30% oxygen and titrate, up or down, to the SpO₂ targets for her age in minutes.",
             "Keep her temperature at 36.5–37.5 °C, including during transfer in a prewarmed incubator.",
             "A glucose plan and an update for the parents are part of stabilisation."],
},

# ---------------------------------------------------------------- 5 · CDH
{
 "id": "n-cdh", "title": "Worse with every breath", "patient": "38 weeks · about 3 kg · no antenatal scans",
 "part": "E", "units": [12, 21], "minutes": 4, "monitor": NEO, "clockLabel": "Since birth", "clock0": 120,
 "brief": "A 38-week baby with no antenatal scans has had respiratory distress since birth. Your colleague has started mask PPV.",
 "start": "n1",
 "nodes": {
  "n1": N("<p>The chest is moving with each breath, yet with every minute of mask ventilation the saturation falls and the heart rate drops.</p>",
          "What do you do?", [
     O("Stop and examine: the abdomen, where the heart sounds are loudest, and the breath sounds on each side.",
       "When a correctly performed intervention makes a baby worse, stop and look at the baby. The findings decide what comes next.", ok=True, to="n2", dt=30, mark="exam"),
     O("Increase the PIP to 40 cm H₂O.", "Doing more of the same without a diagnosis makes this worse. Examine first.", dt=60),
     O("Increase the oxygen to 100% and keep ventilating by mask.", "Oxygen may be needed, but mask ventilation is making this baby worse. Find out why.", dt=60),
     O("Start chest compressions.", "HR is above 60/min and the problem has not been diagnosed. Compressions are not indicated.", crit=True, dt=30),
   ], hr=110, spo2=70, fio2="21", flag="Mask PPV"),
  "n2": N("<p>The abdomen is scaphoid, breath sounds are reduced on the left, and the heart sounds are loudest on the right.</p>",
          "What is the diagnosis, and what do you do?", [
     O("Congenital diaphragmatic hernia: stop mask ventilation, intubate, put an orogastric tube on suction, and ventilate gently.",
       "Mask ventilation inflates the bowel in the chest and compresses the lungs further. Intubation and gastric decompression stop that.", ok=True, to="n3", dt=180, mark="ett"),
     O("Left tension pneumothorax: needle decompression.",
       "A scaphoid abdomen and a displaced heart point to CDH. A needle in the left chest could puncture bowel.", crit=True, dt=60),
     O("Continue mask PPV, but more slowly.", "Any mask ventilation keeps inflating the bowel. Intubate and decompress the stomach.", dt=60),
   ], hr=100, spo2=65, fio2="60", flag="Scaphoid abdomen"),
  "n3": N("<p>He is intubated and ventilated, with the orogastric tube on suction. The heart rate is 140/min and the pre-ductal SpO₂ is 82% and slowly rising.</p>",
          "What next?", [
     O("Ventilate gently (avoid high pressures), monitor pre-ductal SpO₂, and refer urgently to a centre with neonatal surgery: call now and state the transfer time aloud.",
       "Stabilisation and referral are the priority; the repair comes later, in a surgical centre.", ok=True, to="end", dt=600),
     O("Repair the hernia now in the district hospital.", "Repair comes after stabilisation, in a surgical centre. The urgent step is referral.", dt=60),
     O("Extubate him onto CPAP now that he has improved.", "CPAP and mask pressure both inflate the bowel in CDH. Keep him intubated with the stomach decompressed.", crit=True, dt=60),
   ], hr=140, spo2=82, fio2="60"),
  "end": E("good", "<p>The surgical centre accepts him. He is transferred intubated, with gastric decompression, and the hernia is repaired on day 3.</p>",
           hr=146, spo2=88, fio2="50"),
 },
 "timers": [{"mark": "exam", "label": "Stopped to examine", "target": "as soon as he got worse despite correct PPV (≤ 3:00)", "max": 180}],
 "debrief": ["When a correct intervention makes a baby worse, stop and examine him.",
             "A scaphoid abdomen, reduced breath sounds and a displaced heart suggest congenital diaphragmatic hernia.",
             "In CDH, avoid mask PPV and CPAP: intubate and put an orogastric tube on suction.",
             "Ventilate gently, watch the pre-ductal saturation, and refer urgently to a centre with neonatal surgery."],
},

# ---------------------------------------------------------------- 6 · cooling window
{
 "id": "n-cool", "title": "The cooling window", "patient": "38 weeks · uterine rupture · district hospital, no cooling",
 "part": "E", "units": [20], "minutes": 4, "monitor": ["hr", "spo2", "temp"], "clockLabel": "Since birth", "clock0": 2700,
 "brief": "District hospital, no cooling facility. A 38-week baby born after uterine rupture needed 6 minutes of PPV and chest compressions.",
 "start": "n1",
 "nodes": {
  "n1": N("<p>At 45 minutes of life she is lethargic and hypotonic, with no suck. The cord gas shows pH 6.92 and a base deficit of 18 mmol/L.</p>",
          "What is the single most time-critical action?", [
     O("Call the cooling centre now to arrange transfer: where cooling is offered, it must start within 6 hours of birth, and the transfer is the slow step.",
       "The information you need is available now: a significant resuscitation, a cord gas with pH ≤7.0 and base deficit ≥16 within the first hour, and encephalopathy on examination. The limiting step is transfer, not diagnosis, and the decision to cool belongs to the receiving centre.", ok=True, to="n2", dt=600, mark="call", mt=60),
     O("Wait for an EEG and a repeat gas before deciding.",
       "The information needed is available now. The 6-hour window runs out while you wait.", dt=3600),
     O("Start cooling here with ice packs to save time.",
       "Improvised cooling without monitoring risks severe hypothermia, and the evidence for cooling comes from intensive care settings. Do not improvise: call the cooling centre.", crit=True, dt=600),
     O("Observe her overnight and refer if she has seizures.", "By the morning the window has closed. Refer on today's findings.", crit=True, dt=3600),
   ], hr=150, spo2=96, temp="36.9", flag="Encephalopathy"),
  "n2": N("<p>The cooling centre accepts her, and the transport will arrive in 2 hours.</p>",
          "While you wait, what do you do about her temperature?", [
     O("Avoid both hyperthermia and excessive cooling: follow the cooling centre's instructions exactly on how to use the warmer, and record her temperature every 15–30 minutes.",
       "Hyperthermia worsens brain injury, and uncontrolled cooling can overshoot. Follow the referral centre's plan and document it.", ok=True, to="n3", dt=3600, mark="temp", mt=60),
     O("Keep her under the radiant warmer on full so she does not get cold.", "Overheating an asphyxiated baby worsens the injury. Avoid hyperthermia.", crit=True, dt=1800),
     O("Cover her with ice packs until she reaches 33 °C.",
       "Uncontrolled cooling can overshoot to dangerous hypothermia. Only controlled cooling, in a unit that can monitor it.", crit=True, dt=1800),
   ], hr=148, spo2=96, temp="37.4"),
  "n3": N("<p>At 2 hours of life she has rhythmic jerking of the right arm. Capillary glucose is 1.8 mmol/L (32 mg/dL).</p>", "What now?", [
     O("Treat the hypoglycaemia (IV 10% dextrose bolus, then an infusion), treat the seizure according to your protocol, recheck the glucose, and update the cooling centre.",
       "Hypoglycaemia adds to the brain injury and can itself cause seizures. Correct it at once, and keep the receiving team informed.", ok=True, to="end", dt=1200),
     O("Give an anticonvulsant only; the glucose can wait.", "Hypoglycaemia causes seizures and adds brain injury. Correct it now.", crit=True, dt=600),
     O("Feed her by mouth.", "A lethargic baby with no suck cannot feed safely. Give IV dextrose.", dt=600),
   ], hr=162, spo2=94, temp="36.9", flag="Seizure"),
  "end": E("good", "<p>She reaches the cooling centre at 3 hours 40 minutes of life and cooling starts within the window. Her glucose is 4.1 mmol/L on the infusion.</p>",
           hr=140, spo2=97, temp="36.8"),
 },
 "timers": [{"mark": "call", "label": "Cooling centre called", "target": "within the first hour of life", "max": 3600}],
 "debrief": ["After a significant resuscitation, assess every baby for encephalopathy: the history, the cord gas, and the examination.",
             "Where cooling is offered, it must start within 6 hours of birth. Transfer is the slow step, so call the cooling centre early.",
             "Cooling works through the system that delivers it: high-income trials showed benefit, but HELIX (South Asia) found no benefit and a mortality signal. Refer to a centre that cools within its own protocol, and never improvise.",
             "While you wait: avoid both hyperthermia and excessive cooling, and follow the cooling centre's instructions. Never improvise with ice.",
             "Check the glucose. Hypoglycaemia and seizures add to the injury.",
             "Build a system: a written protocol, one phone number, and permission for anyone to call at 3 a.m."],
},
]
